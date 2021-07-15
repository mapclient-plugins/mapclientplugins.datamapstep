# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datamapwidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins.datamapstep.view.nodeeditorsceneviewerwidget import NodeEditorSceneviewerWidget


class Ui_DataMapper(object):
    def setupUi(self, DataMapper):
        if not DataMapper.objectName():
            DataMapper.setObjectName("DataMapper")
        DataMapper.resize(1248, 912)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DataMapper.sizePolicy().hasHeightForWidth())
        DataMapper.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(DataMapper)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dockWidget = QDockWidget(DataMapper)
        self.dockWidget.setObjectName("dockWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dockWidget.sizePolicy().hasHeightForWidth())
        self.dockWidget.setSizePolicy(sizePolicy1)
        self.dockWidget.setMinimumSize(QSize(474, 135))
        self.dockWidget.setFeatures(QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        sizePolicy1.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy1)
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName("scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 472, 862))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.mapButton = QPushButton(self.frame_2)
        self.mapButton.setObjectName("mapButton")

        self.horizontalLayout_2.addWidget(self.mapButton)

        self.horizontalSpacer_2 = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_7.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.displayMisc_frame = QFrame(self.groupBox)
        self.displayMisc_frame.setObjectName("displayMisc_frame")
        self.displayMisc_frame.setFrameShape(QFrame.StyledPanel)
        self.displayMisc_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.displayMisc_frame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.displayAxes_checkBox = QCheckBox(self.displayMisc_frame)
        self.displayAxes_checkBox.setObjectName("displayAxes_checkBox")

        self.horizontalLayout_8.addWidget(self.displayAxes_checkBox)

        self.displaytMisc_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.displaytMisc_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.displayMisc_frame)

        self.displayData_frame = QFrame(self.groupBox)
        self.displayData_frame.setObjectName("displayData_frame")
        self.displayData_frame.setFrameShape(QFrame.StyledPanel)
        self.displayData_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.displayData_frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.displayDataPoints_checkBox_2 = QCheckBox(self.displayData_frame)
        self.displayDataPoints_checkBox_2.setObjectName("displayDataPoints_checkBox_2")

        self.horizontalLayout_10.addWidget(self.displayDataPoints_checkBox_2)

        self.displayDataProjections_checkBox_2 = QCheckBox(self.displayData_frame)
        self.displayDataProjections_checkBox_2.setObjectName("displayDataProjections_checkBox_2")

        self.horizontalLayout_10.addWidget(self.displayDataProjections_checkBox_2)

        self.displayDataProjectionPoints_checkBox_2 = QCheckBox(self.displayData_frame)
        self.displayDataProjectionPoints_checkBox_2.setObjectName("displayDataProjectionPoints_checkBox_2")

        self.horizontalLayout_10.addWidget(self.displayDataProjectionPoints_checkBox_2)

        self.displayData_horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.displayData_horizontalSpacer_2)


        self.verticalLayout_3.addWidget(self.displayData_frame)

        self.displayNodes_frame = QFrame(self.groupBox)
        self.displayNodes_frame.setObjectName("displayNodes_frame")
        self.displayNodes_frame.setFrameShape(QFrame.StyledPanel)
        self.displayNodes_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.displayNodes_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.displayNodePoints_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodePoints_checkBox.setObjectName("displayNodePoints_checkBox")

        self.horizontalLayout_6.addWidget(self.displayNodePoints_checkBox)

        self.displayNodeNumbers_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeNumbers_checkBox.setObjectName("displayNodeNumbers_checkBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.displayNodeNumbers_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeNumbers_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.displayNodeNumbers_checkBox)

        self.displayNodeDerivatives_checkBox = QCheckBox(self.displayNodes_frame)
        self.displayNodeDerivatives_checkBox.setObjectName("displayNodeDerivatives_checkBox")
        sizePolicy3.setHeightForWidth(self.displayNodeDerivatives_checkBox.sizePolicy().hasHeightForWidth())
        self.displayNodeDerivatives_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_6.addWidget(self.displayNodeDerivatives_checkBox)

        self.displayNodes_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.displayNodes_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.displayNodes_frame)

        self.displayElements_frame = QFrame(self.groupBox)
        self.displayElements_frame.setObjectName("displayElements_frame")
        self.displayElements_frame.setFrameShape(QFrame.StyledPanel)
        self.displayElements_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.displayElements_frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.displayElementNumbers_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementNumbers_checkBox.setObjectName("displayElementNumbers_checkBox")

        self.horizontalLayout_4.addWidget(self.displayElementNumbers_checkBox)

        self.displayElementAxes_checkBox = QCheckBox(self.displayElements_frame)
        self.displayElementAxes_checkBox.setObjectName("displayElementAxes_checkBox")
        sizePolicy3.setHeightForWidth(self.displayElementAxes_checkBox.sizePolicy().hasHeightForWidth())
        self.displayElementAxes_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_4.addWidget(self.displayElementAxes_checkBox)

        self.displayElements_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.displayElements_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.displayElements_frame)

        self.displayLines_frame = QFrame(self.groupBox)
        self.displayLines_frame.setObjectName("displayLines_frame")
        self.displayLines_frame.setFrameShape(QFrame.StyledPanel)
        self.displayLines_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.displayLines_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.displayLines_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLines_checkBox.setObjectName("displayLines_checkBox")

        self.horizontalLayout_5.addWidget(self.displayLines_checkBox)

        self.displayLinesExterior_checkBox = QCheckBox(self.displayLines_frame)
        self.displayLinesExterior_checkBox.setObjectName("displayLinesExterior_checkBox")
        sizePolicy3.setHeightForWidth(self.displayLinesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displayLinesExterior_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_5.addWidget(self.displayLinesExterior_checkBox)

        self.displayLines_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.displayLines_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.displayLines_frame)

        self.displaySurfaces_frame = QFrame(self.groupBox)
        self.displaySurfaces_frame.setObjectName("displaySurfaces_frame")
        self.displaySurfaces_frame.setFrameShape(QFrame.StyledPanel)
        self.displaySurfaces_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.displaySurfaces_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.displaySurfaces_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfaces_checkBox.setObjectName("displaySurfaces_checkBox")

        self.horizontalLayout_3.addWidget(self.displaySurfaces_checkBox)

        self.displaySurfacesExterior_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesExterior_checkBox.setObjectName("displaySurfacesExterior_checkBox")
        sizePolicy3.setHeightForWidth(self.displaySurfacesExterior_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesExterior_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.displaySurfacesExterior_checkBox)

        self.displaySurfacesTranslucent_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesTranslucent_checkBox.setObjectName("displaySurfacesTranslucent_checkBox")
        sizePolicy3.setHeightForWidth(self.displaySurfacesTranslucent_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesTranslucent_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.displaySurfacesTranslucent_checkBox)

        self.displaySurfacesWireframe_checkBox = QCheckBox(self.displaySurfaces_frame)
        self.displaySurfacesWireframe_checkBox.setObjectName("displaySurfacesWireframe_checkBox")
        sizePolicy3.setHeightForWidth(self.displaySurfacesWireframe_checkBox.sizePolicy().hasHeightForWidth())
        self.displaySurfacesWireframe_checkBox.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.displaySurfacesWireframe_checkBox)

        self.displaySurfaces_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.displaySurfaces_horizontalSpacer)


        self.verticalLayout_3.addWidget(self.displaySurfaces_frame)

        self.displayData_frame.raise_()
        self.displayNodes_frame.raise_()
        self.displaySurfaces_frame.raise_()
        self.displayLines_frame.raise_()
        self.displayElements_frame.raise_()
        self.displayMisc_frame.raise_()

        self.verticalLayout.addWidget(self.groupBox)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.viewAllButton = QPushButton(self.frame)
        self.viewAllButton.setObjectName("viewAllButton")

        self.gridLayout.addWidget(self.viewAllButton, 0, 0, 1, 1)

        self.doneButton = QPushButton(self.frame)
        self.doneButton.setObjectName("doneButton")
        sizePolicy3.setHeightForWidth(self.doneButton.sizePolicy().hasHeightForWidth())
        self.doneButton.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.doneButton, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)

        self.dockWidget.setWidget(self.dockWidgetContents)

        self.horizontalLayout.addWidget(self.dockWidget)

        self.sceneviewerWidget = NodeEditorSceneviewerWidget(DataMapper)
        self.sceneviewerWidget.setObjectName("sceneviewerWidget")
        self.sceneviewerWidget.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.sceneviewerWidget.sizePolicy().hasHeightForWidth())
        self.sceneviewerWidget.setSizePolicy(sizePolicy4)
        self.sceneviewerWidget.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.sceneviewerWidget)


        self.retranslateUi(DataMapper)

        QMetaObject.connectSlotsByName(DataMapper)
    # setupUi

    def retranslateUi(self, DataMapper):
        DataMapper.setWindowTitle(QCoreApplication.translate("DataMapper", "Form", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("DataMapper", "Data Mapper", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("DataMapper", "Map", None))
        self.mapButton.setText(QCoreApplication.translate("DataMapper", "Execute", None))
        self.groupBox.setTitle(QCoreApplication.translate("DataMapper", "Display", None))
        self.displayAxes_checkBox.setText(QCoreApplication.translate("DataMapper", "Axes", None))
        self.displayDataPoints_checkBox_2.setText(QCoreApplication.translate("DataMapper", "Data points", None))
        self.displayDataProjections_checkBox_2.setText(QCoreApplication.translate("DataMapper", "Data projections", None))
        self.displayDataProjectionPoints_checkBox_2.setText(QCoreApplication.translate("DataMapper", "Data projection points", None))
        self.displayNodePoints_checkBox.setText(QCoreApplication.translate("DataMapper", "Node points", None))
        self.displayNodeNumbers_checkBox.setText(QCoreApplication.translate("DataMapper", "Node numbers", None))
        self.displayNodeDerivatives_checkBox.setText(QCoreApplication.translate("DataMapper", "Node derivatives", None))
        self.displayElementNumbers_checkBox.setText(QCoreApplication.translate("DataMapper", "Element numbers", None))
        self.displayElementAxes_checkBox.setText(QCoreApplication.translate("DataMapper", "Element axes", None))
        self.displayLines_checkBox.setText(QCoreApplication.translate("DataMapper", "Lines", None))
        self.displayLinesExterior_checkBox.setText(QCoreApplication.translate("DataMapper", "Exterior", None))
        self.displaySurfaces_checkBox.setText(QCoreApplication.translate("DataMapper", "Surfaces", None))
        self.displaySurfacesExterior_checkBox.setText(QCoreApplication.translate("DataMapper", "Exterior", None))
        self.displaySurfacesTranslucent_checkBox.setText(QCoreApplication.translate("DataMapper", "Transluc.", None))
        self.displaySurfacesWireframe_checkBox.setText(QCoreApplication.translate("DataMapper", "Wireframe", None))
#if QT_CONFIG(tooltip)
        self.viewAllButton.setToolTip(QCoreApplication.translate("DataMapper", "Adjust the view to see the whole model", None))
#endif // QT_CONFIG(tooltip)
        self.viewAllButton.setText(QCoreApplication.translate("DataMapper", "View All", None))
#if QT_CONFIG(tooltip)
        self.doneButton.setToolTip(QCoreApplication.translate("DataMapper", "Finish this step", None))
#endif // QT_CONFIG(tooltip)
        self.doneButton.setText(QCoreApplication.translate("DataMapper", "Done", None))
    # retranslateUi

