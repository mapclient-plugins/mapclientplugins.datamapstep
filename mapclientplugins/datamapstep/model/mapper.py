from cmlibs.zinc.context import Context
from cmlibs.utils.zinc.general import ChangeManager
from cmlibs.utils.zinc.finiteelement import get_highest_dimension_mesh
from cmlibs.zinc.field import Field, FieldFindMeshLocation
from cmlibs.zinc.element import Element
from cmlibs.zinc.result import RESULT_OK


class Mapper(object):

    def __init__(self, zinc_model_file_name, zinc_data_file_name):
        self._zinc_model_file_name = zinc_model_file_name
        self._zinc_data_file_name = zinc_data_file_name
        self._context = Context("DataMap")
        self._region = None
        self._field_module = None
        self._model_coordinates_field = None
        self._model_coordinates_field_name = None
        self._data_coordinates_field = None
        self._data_coordinates_field_name = None
        self._find_mesh_location_field = None
        self._stored_mesh_location_field = None
        self._active_data_point_group_field = None
        self._project_surface_group = None
        self._project_surface_element_group = None
        self._marker_group = None
        self._marker_group_name = None
        self._marker_data_group = None
        self._marker_data_coordinates_field = None
        self._marker_data_name_field = None

    def get_context(self):
        return self._context

    def get_region(self):
        return self._region

    def get_field_module(self):
        return self._field_module

    def get_data_coordinate_field(self):
        return self._data_coordinates_field

    def get_model_coordinate_field(self):
        return self._model_coordinates_field

    def get_active_data_point_group_field(self):
        return self._active_data_point_group_field

    def get_data_projection_delta_coordinate_field(self):
        return self._data_projection_delta_coordinate_field

    def get_data_projection_error_field(self):
        return self._data_projection_error_field

    def get_marker_group(self):
        return self._marker_group

    # combo_box.setPlaceholderText() is currently broken. If this method gets fixed we should update (simplify) the
    # following two methods by removing the dummy elements (---) and using setPlaceholderText in datamapwidget.py.
    def update_model_coordinates_field(self, field_name):
        field = self._field_module.findFieldByName(field_name)
        finite_element_field = field.castFiniteElement()
        self._model_coordinates_field = finite_element_field

    def update_data_coordinates_field(self, field_name):
        with ChangeManager(self._field_module):
            data_points = self._field_module.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)

            field_group = self._field_module.createFieldGroup()
            tmp_true = self._field_module.createFieldConstant([1])
            active_datapoints_group = field_group.createNodesetGroup(data_points)
            active_datapoints_group.addNodesConditional(tmp_true)

        field = self._field_module.findFieldByName(field_name)
        self._data_coordinates_field = field

    def get_field_list(self):
        field_list = []

        field_iterator = self._field_module.createFielditerator()
        field = field_iterator.next()
        while field.isValid():
            if field.isTypeCoordinate() and (field.getNumberOfComponents() == 3) and (field.castFiniteElement().isValid()):
                field_list.append(field.getName())
            field = field_iterator.next()

        return field_list

    def load(self):
        self._region = self._context.createRegion()
        self._field_module = self._region.getFieldmodule()
        self._load_model()
        self._load_data()
        # self._calculate_data_projections()

    def _load_model(self):
        result = self._region.readFile(self._zinc_model_file_name)
        assert result == RESULT_OK, "Failed to load model file" + str(self._zinc_model_file_name)
        self._mesh = [self._field_module.findMeshByDimension(d + 1) for d in range(3)]

    def _load_data(self):
        sir = self._region.createStreaminformationRegion()
        data_resource = sir.createStreamresourceFile(self._zinc_data_file_name)
        sir.setResourceDomainTypes(data_resource, Field.DOMAIN_TYPE_NODES)
        result = self._region.read(sir)
        assert result == RESULT_OK, "Failed to load data file" + str(self._zinc_data_file_name)

    def _get_project_face_mesh_group(self):
        fm = self._region.getFieldmodule()
        mesh2d = fm.findMeshByDimension(2)

        is_exterior = fm.createFieldIsExterior()
        is_on_face_xi3_1 = fm.createFieldIsOnFace(Element.FACE_TYPE_XI3_1)
        is_both = fm.createFieldAnd(is_exterior, is_on_face_xi3_1)
        self._exterior_surface_field = is_both

        field_group = self._field_module.createFieldGroup()
        field_group.setName('exteriorFaceElementGroup')
        self._exterior_face_mesh_group = field_group.createMeshGroup(mesh2d)
        result = self._exterior_face_mesh_group.addElementsConditional(is_both)

    def map(self):
        self._calculate_data_projections()

    def _calculate_data_projections(self):
        self._get_project_face_mesh_group()

        # mesh2d = self._exterior_face_mesh_group.getMasterMesh()
        mesh3d = get_highest_dimension_mesh(self._field_module)

        if self._find_mesh_location_field is None and self._exterior_face_mesh_group is not None:
            self._find_mesh_location_field = self._field_module.createFieldFindMeshLocation(
                self._data_coordinates_field,
                self._model_coordinates_field,
                mesh3d)

            if self._find_mesh_location_field.isValid():
                self._find_mesh_location_field.setSearchMode(FieldFindMeshLocation.SEARCH_MODE_NEAREST)
                # self._find_mesh_location_field.setSearchMode(FieldFindMeshLocation.SEARCH_MODE_EXACT)
            else:
                self._find_mesh_location_field = None
                raise ValueError('Failed to create find mesh location field.')

        if self._stored_mesh_location_field is None:
            self._stored_mesh_location_field = self._field_module.createFieldStoredMeshLocation(mesh3d)
            self._stored_mesh_location_field.setName('stored_location')
            if not self._stored_mesh_location_field.isValid():
                self._stored_mesh_location_field = None
                raise ValueError('Failed to create stored mesh location field.')

        datapoints = self._field_module.findNodesetByFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
        field_group = self._field_module.createFieldGroup()
        tmp_true = self._field_module.createFieldConstant([1])
        active_datapoints_group = field_group.createNodesetGroup(datapoints)
        active_datapoints_group.addNodesConditional(tmp_true)
        dimension = mesh3d.getDimension()

        with ChangeManager(self._field_module):
            self._data_projection_coordinate_field = self._field_module.createFieldEmbedded(
                self._model_coordinates_field,
                self._stored_mesh_location_field)
            self._data_projection_delta_coordinate_field = self._field_module.createFieldSubtract(
                self._data_projection_coordinate_field,
                self._data_coordinates_field)

            self._data_projection_error_field = self._field_module.createFieldMagnitude(
                self._data_projection_delta_coordinate_field)

            nodetemplate = datapoints.createNodetemplate()
            nodetemplate.defineField(self._stored_mesh_location_field)
            cache = self._field_module.createFieldcache()
            data_iter = active_datapoints_group.createNodeiterator()
            datapoint = data_iter.next()
            xi3 = []
            while datapoint.isValid():
                cache.setNode(datapoint)
                element, xi = self._find_mesh_location_field.evaluateMeshLocation(cache, dimension)
                if element.isValid():
                    # print("Element {} | xi {}".format(element.getIdentifier(), xi))
                    xi3.append(xi[2])
                    datapoint.merge(nodetemplate)
                    result = self._stored_mesh_location_field.assignMeshLocation(cache, element, xi)
                    if result != RESULT_OK:
                        print("Shouldn't be here!")
                datapoint = data_iter.next()
            # print('end of embedding...')

    def write(self, location):
        self._region.writeFile(location + '/mapped.exf')
