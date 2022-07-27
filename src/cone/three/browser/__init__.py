from cone.app.browser.resources import resources
from cone.app.browser.resources import set_resource_include
import webresource as wr
import os


resources_dir = os.path.join(os.path.dirname(__file__), 'static')


# threejs
threejs_resources = wr.ResourceGroup(
    name='cone.three',
    directory=os.path.join(resources_dir, 'threejs'),
    path='threejs',
    group=resources
)
threejs_resources.add(wr.ScriptResource(
    name='three-js',
    resource='three.js',
    compressed='three.min.js'
))


def configure_resources(settings):
    set_resource_include(settings, 'three-js', 'authenticated')
