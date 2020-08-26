import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class DatasetpreviewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datasetpreview')

    ## ITemplateHelpers
    def get_helpers(self):
        from ckanext.datasetpreview import helpers as dsp_helpers
        return {
            'get_preview_chart_data': dsp_helpers.get_preview_chart_data
        }