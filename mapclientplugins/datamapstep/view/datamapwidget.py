from PySide6 import QtWidgets

from .ui_datamapwidget import Ui_DataMapper


class DataMapWidget(QtWidgets.QWidget):

    def __init__(self, model, parent=None):
        super(DataMapWidget, self).__init__(parent)
        self._ui = Ui_DataMapper()
        self._ui.setupUi(self)
        self._ui.sceneviewerWidget.setContext(model.get_context())
        self._ui.sceneviewerWidget.graphicsInitialized.connect(self._graphics_initialized)
        self._model = model
        self._populate_field_combo_boxes()
        self._done_callback = None
        self._glyph_size_changed()
        self._make_connections()

    def _graphics_initialized(self):
        self._model.create_graphics()
        self._glyph_size_changed()

    def _graphics_updated(self):
        self._scene_changed()
        scene_viewer = self._ui.sceneviewerWidget.getSceneviewer()
        if scene_viewer is not None:
            scene_viewer.viewAll()

    def _refresh_graphics(self):
        self._ui.sceneviewerWidget.paintGL()
        # self._model.autorange_spectrum()

    def _scene_changed(self):
        sceneviewer = self._ui.sceneviewerWidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setScene(self._model.get_scene())
            self._refresh_graphics()

    def register_done_execution(self, done_callback):
        self._done_callback = done_callback

    def _make_connections(self):
        self._ui.mapButton.clicked.connect(self._map_clicked)
        self._ui.doneButton.clicked.connect(self._done_clicked)
        self._ui.model_field_comboBox.currentTextChanged.connect(self._model_field_chosen)
        self._ui.data_field_comboBox.currentTextChanged.connect(self._data_field_chosen)
        self._ui.glyph_size_spinBox.valueChanged.connect(self._glyph_size_changed)

    def _map_clicked(self):
        self._model.map()

    def _done_clicked(self):
        self._model.write()
        self._done_callback()

    def _populate_field_combo_boxes(self):
        field_list = self._model.get_field_list()
        field_list = ["---"] + field_list
        self._ui.model_field_comboBox.addItems(field_list)
        self._ui.data_field_comboBox.addItems(field_list)

    def _model_field_chosen(self):
        try:
            self._model.update_model_coordinates_field(self._ui.model_field_comboBox.currentText())
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, 'Warning', str(e))
            self._ui.model_field_comboBox.setCurrentIndex(0)
            self._model.update_model_coordinates_field(self._ui.model_field_comboBox.currentText())
        self._graphics_updated()

    def _data_field_chosen(self):
        try:
            self._model.update_data_coordinates_field(self._ui.data_field_comboBox.currentText())
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, 'Warning', str(e))
            self._ui.data_field_comboBox.setCurrentIndex(0)
            self._model.update_data_coordinates_field(self._ui.data_field_comboBox.currentText())
        self._graphics_updated()

    def _glyph_size_changed(self):
        self._model.update_glyph_size(self._ui.glyph_size_spinBox.value())
        self._graphics_updated()
