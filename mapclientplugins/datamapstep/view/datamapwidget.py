from PySide import QtGui, QtCore

from .ui_datamapwidget import Ui_DataMapper


class DataMapWidget(QtGui.QWidget):

    def __init__(self, model, parent=None):
        super(DataMapWidget, self).__init__(parent)
        self._ui = Ui_DataMapper()
        self._ui.setupUi(self)
        self._ui.sceneviewerWidget.setContext(model.get_context())
        self._ui.sceneviewerWidget.graphicsInitialized.connect(self._graphics_initialized)
        self._model = model
        self._done_callback = None
        self._make_connections()

    def _graphics_initialized(self):
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
            self._model.create_graphics()
            sceneviewer.setScene(self._model.get_scene())
            self._refresh_graphics()

    def register_done_execution(self, done_callback):
        self._done_callback = done_callback

    def _make_connections(self):
        self._ui.mapButton.clicked.connect(self._map_clicked)
        self._ui.doneButton.clicked.connect(self._done_clicked)

    def _map_clicked(self):
        self._model.map()

    def _done_clicked(self):
        self._model.write()
        self._done_callback()
