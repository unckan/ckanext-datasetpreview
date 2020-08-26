import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class DatasetpreviewPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(plugins.IRoutes, inherit=True)
    
    # IConfigurer
    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datasetpreview')

    ## ITemplateHelpers
    def get_helpers(self):
        from ckanext.datasetpreview import helpers as dsp_helpers
        return {
            'helper_test': dsp_helpers.helper_test
        }
    
    ## IRoutes
    def before_map(self, map):
        controller = 'ckanext.datasetpreview.controllers:ViewController'
        map.connect('big_chart_viewer', '/chart', controller=controller, action='chart')
        
        return map