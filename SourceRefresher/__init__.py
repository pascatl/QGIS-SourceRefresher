# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SourceRefresher
                                 A QGIS plugin
 The Source Refresher refreshes a database connection
                             -------------------
        begin                : 2018-10-25
        copyright            : (C) 2018 by Stadt Erlangen/eGov/GIS
        email                : gis@stadt.erlangen.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SourceRefresher class from file SourceRefresher.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .source_refresher import SourceRefresher
    return SourceRefresher(iface)
