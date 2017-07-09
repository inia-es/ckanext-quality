import ckan.plugins as p


class Quality(p.SingletonPlugin):
    '''Dataset quality based on metadata'''

    p.implements(p.IRoutes,inherit=True)
    p.implements(p.IConfigurer)

    def before_map(self, map):
 	       

	map.connect('add dataset', '/dataset/new',controller='ckanext.quality.package:PackageController', action='new')          
 	

        
        return map

    def after_map(self, map):
	

	map.connect('add dataset', '/dataset/new',controller='ckanext.quality.package:PackageController', action='new')          

        return map



    def update_config(self, config_):
        p.toolkit.add_template_directory(config_, 'templates')
        p.toolkit.add_public_directory(config_, 'public')
        p.toolkit.add_resource('fanstatic', 'quality')
