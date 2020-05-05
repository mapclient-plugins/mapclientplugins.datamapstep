import os

from opencmiss.zinc.field import Field
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.material import Material
from opencmiss.utils.zinc.general import ChangeManager

from .mapper import Mapper

from math import sqrt


def magnitude(v):
    return sqrt(sum(v[i] * v[i] for i in range(len(v))))


def sub(u, v):
    return [u[i] - v[i] for i in range(len(u))]


class MappingModel(object):

    def __init__(self, input_zinc_model_file, input_zinc_data_file, location):
        self._mapper = Mapper(input_zinc_model_file, input_zinc_data_file)
        self._mapper.load()
        self._context = self._mapper.get_context()
        self._region = self._mapper.get_region()
        self._scene = self._region.getScene()
        self._location = location

        self._initialise_graphics_module()

    def get_context(self):
        return self._context

    def get_region(self):
        return self._region

    def get_scene(self):
        return self._region.getScene()

    def _initialise_graphics_module(self):
        self._material_module = self._context.getMaterialmodule()
        with ChangeManager(self._material_module):
            self._material_module.defineStandardMaterials()
            trans_blue = self._material_module.createMaterial()
            trans_blue.setName("trans_blue")
            trans_blue.setManaged(True)
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_AMBIENT, [0.0, 0.2, 0.6])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_DIFFUSE, [0.0, 0.7, 1.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_EMISSION, [0.0, 0.0, 0.0])
            trans_blue.setAttributeReal3(Material.ATTRIBUTE_SPECULAR, [0.1, 0.1, 0.1])
            trans_blue.setAttributeReal(Material.ATTRIBUTE_ALPHA, 0.3)
            trans_blue.setAttributeReal(Material.ATTRIBUTE_SHININESS, 0.2)
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()
        tessellation_module = self._context.getTessellationmodule()
        default_tessellation = tessellation_module.getDefaultTessellation()
        default_tessellation.setRefinementFactors([12])

    def _hide_data_projections(self):
        scene = self._region.getScene()
        with ChangeManager(scene):
            graphics = scene.findGraphicsByName('data-projections')
            if graphics.isValid():
                scene.removeGraphics(graphics)
            graphics = scene.findGraphicsByName('data-mean-error')
            if graphics.isValid():
                scene.removeGraphics(graphics)
            graphics = scene.findGraphicsByName('data-maximum-error')
            if graphics.isValid():
                scene.removeGraphics(graphics)

    def _autorange_spectrum(self):
        scene = self._region.getScene()
        spectrum_module = scene.getSpectrummodule()
        spectrum = spectrum_module.getDefaultSpectrum()
        scene_filter_module = scene.getScenefiltermodule()
        scene_filter = scene_filter_module.getDefaultScenefilter()
        spectrum.autorange(scene, scene_filter)

    def create_graphics(self):
        model_coordinates = self._mapper.get_model_coordinate_field()
        data_coordinate = self._mapper.get_data_coordinate_field()
        with ChangeManager(self._scene):
            self._scene.removeAllGraphics()
            data_points = self._scene.createGraphicsPoints()
            data_points.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            data_points.setCoordinateField(data_coordinate)
            point_attr = data_points.getGraphicspointattributes()
            point_attr.setBaseSize([0.05, 0.05, 0.05])
            point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_SPHERE)
            data_points.setMaterial(self._material_module.findMaterialByName("yellow"))
            data_points.setName("displayMarkerDataPoints")
            data_points.setVisibilityFlag(True)

            lines = self._scene.createGraphicsLines()
            lines.setCoordinateField(model_coordinates)
            lines.setExterior(True)
            lines.setName("displayLines")
            lines.setVisibilityFlag(True)

            mesh_dimension = 2
            surfaces = self._scene.createGraphicsSurfaces()
            surfaces.setCoordinateField(model_coordinates)
            surfaces.setRenderPolygonMode(Graphics.RENDER_POLYGON_MODE_SHADED)
            surfaces.setExterior(True if (mesh_dimension == 3) else False)
            surfaces_material = self._material_module.findMaterialByName("trans_blue")
            surfaces.setMaterial(surfaces_material)
            surfaces.setName("displaySurfaces")
            surfaces.setVisibilityFlag(True)

            self._hide_data_projections()
            scene = self._region.getScene()

            data_coordinate_field = self._mapper.get_data_coordinate_field()
            active_data_coordinate_field = self._mapper.get_active_data_point_group_field()
            data_projection_delta_coordinate_field = self._mapper.get_data_projection_delta_coordinate_field()
            data_projection_error_field = self._mapper.get_data_projection_error_field()
            spectrum_module = scene.getSpectrummodule()
            default_spectrum = spectrum_module.getDefaultSpectrum()

            error_bars = scene.createGraphicsPoints()
            error_bars.setName('data-projections')
            error_bars.setFieldDomainType(Field.DOMAIN_TYPE_DATAPOINTS)
            error_bars.setCoordinateField(data_coordinate_field)
            # error_bars.setSubgroupField(active_data_coordinate_field)
            point_attr = error_bars.getGraphicspointattributes()
            point_attr.setGlyphShapeType(Glyph.SHAPE_TYPE_LINE)
            point_attr.setBaseSize([0.0, 1.0, 1.0])
            point_attr.setScaleFactors([1.0, 0.0, 0.0])
            point_attr.setOrientationScaleField(data_projection_delta_coordinate_field)
            error_bars.setDataField(data_projection_error_field)
            error_bars.setSpectrum(default_spectrum)
            error_bars.setVisibilityFlag(True)
            self._autorange_spectrum()

    def write(self):
        self._mapper.write(self._location)
