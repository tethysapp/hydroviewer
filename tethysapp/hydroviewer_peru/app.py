from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting, SpatialDatasetServiceSetting
from tethys_sdk.permissions import Permission, PermissionGroup

base_name = __package__.split('.')[-1]
base_url = base_name.replace('_', '-')

class Hydroviewer(TethysAppBase):

    name = 'HydroViewer Peru'
    index = '{0}:home'.format(base_name)
    icon = '{0}/images/peru-icon.png'.format(base_name)
    package = '{0}'.format(base_name)
    root_url = base_url
    color = '#00374b'
    description = 'This is the Hydroviewer App customized for Peru.'
    tags = '"Hydrology", "GEOGloWS", "Hydroviewer"'
    enable_feedback = False
    feedback_emails = []

    def spatial_dataset_service_settings(self):
        """
        Spatial_dataset_service_settings method.
        """
        sds_settings = (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

        return sds_settings

    def url_maps(self):
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url=base_url,
                controller='{0}.controllers.home'.format(base_name)),
            UrlMap(
                name='ecmwf',
                url='ecmwf-rapid',
                controller='{0}.controllers.ecmwf'.format(base_name)),
            UrlMap(
                name='lis',
                url='lis-rapid',
                controller='{0}.controllers.lis'.format(base_name)),
            UrlMap(
                name='hiwat',
                url='hiwat-rapid',
                controller='{0}.controllers.hiwat'.format(base_name)),
            UrlMap(
                name='get-available-dates',
                url='get-available-dates',
                controller='{0}.controllers.get_available_dates'.format(base_name)),
            UrlMap(
                name='get-available-dates',
                url='ecmwf-rapid/get-available-dates',
                controller='{0}.controllers.get_available_dates'.format(base_name)),
            UrlMap(
                name='get-time-series',
                url='get-time-series',
                controller='{0}.controllers.ecmwf_get_time_series'.format(base_name)),
            UrlMap(
                name='get-time-series',
                url='ecmwf-rapid/get-time-series',
                controller='{0}.controllers.ecmwf_get_time_series'.format(base_name)),
            UrlMap(
                name='get-warning-points',
                url='get-warning-points',
                controller='{0}.controllers.get_warning_points'.format(base_name)),
            UrlMap(
                name='get-warning-points',
                url='ecmwf-rapid/get-warning-points',
                controller='{0}.controllers.get_warning_points'.format(base_name)),
            UrlMap(
                name='get-historic-data',
                url='get-historic-data',
                controller='{0}.controllers.get_historic_data'.format(base_name)),
            UrlMap(
                name='get-flow-duration-curve',
                url='get-flow-duration-curve',
                controller='{0}.controllers.get_flow_duration_curve'.format(base_name)),
            UrlMap(
                name='get-daily-seasonal-streamflow',
                url='get-daily-seasonal-streamflow',
                controller='{0}.controllers.get_daily_seasonal_streamflow'.format(base_name)),
            UrlMap(
                name='get-monthly-seasonal-streamflow',
                url='get-monthly-seasonal-streamflow',
                controller='{0}.controllers.get_monthly_seasonal_streamflow'.format(base_name)),
            UrlMap(
                name='get_historic_data_csv',
                url='get-historic-data-csv',
                controller='{0}.controllers.get_historic_data_csv'.format(base_name)),
            UrlMap(
                name='get_forecast_data_csv',
                url='get-forecast-data-csv',
                controller='{0}.controllers.get_forecast_data_csv'.format(base_name)),
            UrlMap(
                name='get-historic-data',
                url='ecmwf-rapid/get-historic-data',
                controller='{0}.controllers.get_historic_data'.format(base_name)),
            UrlMap(
                name='get-flow-duration-curve',
                url='ecmwf-rapid/get-flow-duration-curve',
                controller='{0}.controllers.get_flow_duration_curve'.format(base_name)),
            UrlMap(
                name='get-daily-seasonal-streamflow',
                url='ecmwf-rapid/get-daily-seasonal-streamflow',
                controller='{0}.controllers.get_daily_seasonal_streamflow'.format(base_name)),
            UrlMap(
                name='get-monthly-seasonal-streamflow',
                url='ecmwf-rapid/get-monthly-seasonal-streamflow',
                controller='{0}.controllers.get_monthly_seasonal_streamflow'.format(base_name)),
            UrlMap(
                name='get_historic_data_csv',
                url='ecmwf-rapid/get-historic-data-csv',
                controller='{0}.controllers.get_historic_data_csv'.format(base_name)),
            UrlMap(
                name='get_forecast_data_csv',
                url='ecmwf-rapid/get-forecast-data-csv',
                controller='{0}.controllers.get_forecast_data_csv'.format(base_name)),
            UrlMap(
                name='get_lis_shp',
                url='get-lis-shp',
                controller='{0}.controllers.shp_to_geojson'.format(base_name)),
            UrlMap(
                name='get_lis_shp',
                url='lis-rapid/get-lis-shp',
                controller='{0}.controllers.shp_to_geojson'.format(base_name)),
            UrlMap(
                name='get_hiwat_shp',
                url='get-hiwat-shp',
                controller='{0}.controllers.shp_to_geojson'.format(base_name)),
            UrlMap(
                name='get_hiwat_shp',
                url='hiwat-rapid/get-hiwat-shp',
                controller='{0}.controllers.shp_to_geojson'.format(base_name)),
            UrlMap(
                name='set_def_ws',
                url='admin/setdefault',
                controller='{0}.controllers.setDefault'.format(base_name)),
            UrlMap(
                name='set_def_ws',
                url='ecmwf-rapid/admin/setdefault',
                controller='{0}.controllers.setDefault'.format(base_name)),
            UrlMap(
                name='set_def_ws',
                url='lis-rapid/admin/setdefault',
                controller='{0}.controllers.setDefault'.format(base_name)),
            UrlMap(
                name='forecastpercent',
                url='ecmwf-rapid/forecastpercent',
                controller='{0}.controllers.forecastpercent'.format(base_name)),
            UrlMap(
                name='forecastpercent',
                url='forecastpercent',
                controller='{0}.controllers.forecastpercent'.format(base_name)),
        )

        return url_maps

    # def permissions(self):
    #
    #     update_default = Permission(
    #         name='update_default',
    #         description='Update Default Settings'
    #     )
    #
    #     admin = PermissionGroup(
    #         name='admin',
    #         permissions=(update_default,)
    #     )
    #
    #
    #     permissions = (admin,)
    #
    #     return permissions

    def custom_settings(self):
        return (
            CustomSetting(
                name='api_source',
                type=CustomSetting.TYPE_STRING,
                description='Tethys portal where Streamflow Prediction Tool is installed',
                required=True
            ),
            CustomSetting(
                name='workspace',
                type=CustomSetting.TYPE_STRING,
                description='Workspace within Geoserver where web service is',
                required=True
            ),
            CustomSetting(
                name='region',
                type=CustomSetting.TYPE_STRING,
                description='Streamflow Prediction Tool Region',
                required=True
            ),
            CustomSetting(
                name='keywords',
                type=CustomSetting.TYPE_STRING,
                description='Keyword(s) for visualizing watersheds in HydroViewer',
                required=True
            ),
            CustomSetting(
                name='zoom_info',
                type=CustomSetting.TYPE_STRING,
                description='lon,lat,zoom_level',
                required=True
            ),
            CustomSetting(
                name='default_model_type',
                type=CustomSetting.TYPE_STRING,
                description='Default Model Type : (Options : ECMWF-RAPID, LIS-RAPID)',
                required=False
            ),
            CustomSetting(
                name='default_watershed_name',
                type=CustomSetting.TYPE_STRING,
                description='Default Watershed Name: (For ex: "South America (Brazil)") ',
                required=False
            ),
            CustomSetting(
                name='show_dropdown',
                type=CustomSetting.TYPE_BOOLEAN,
                description='Hide Watershed Options when default present (True or False) ',
                required=True,
                value=True
            ),
            CustomSetting(
                name='lis_path',
                type=CustomSetting.TYPE_STRING,
                description='Path to local LIS-RAPID directory',
                required=False
            ),
            CustomSetting(
                name='hiwat_path',
                type=CustomSetting.TYPE_STRING,
                description='Path to local HIWAT-RAPID directory',
                required=False
            ),
        )
