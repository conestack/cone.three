from cone.app.browser.resources import resources
from cone.app.browser.resources import set_resource_include
import webresource as wr
import os


resources_dir = os.path.join(os.path.dirname(__file__), 'static')


# threejs core
threejs_resources = wr.ResourceGroup(
    name='cone.three-threejs',
    directory=os.path.join(resources_dir, 'threejs'),
    path='threejs',
    group=resources
)
threejs_resources.add(wr.ScriptResource(
    name='three-js',
    resource='three.js',
    compressed='three.min.js'
))

# threejs loaders
threejs_loaders_resources = wr.ResourceGroup(
    name='cone.three-loaders',
    directory=os.path.join(resources_dir, 'threejs-loaders'),
    path='threejs-loaders',
    group=resources
)
threejs_loaders_resources.add(wr.ScriptResource(
    name='three-objloader-js',
    depends='three-js',
    resource='OBJLoader.js'
))
threejs_loaders_resources.add(wr.ScriptResource(
    name='three-mtlloader-js',
    depends='three-js',
    resource='MTLLoader.js'
))

# threejs controls
threejs_controls_resources = wr.ResourceGroup(
    name='cone.three-controls',
    directory=os.path.join(resources_dir, 'threejs-controls'),
    path='threejs-controls',
    group=resources
)
threejs_controls_resources.add(wr.ScriptResource(
    name='three-acrballcontrols-js',
    depends='three-js',
    resource='ArcballControls.js'
))
threejs_controls_resources.add(wr.ScriptResource(
    name='three-orbitcontrols-js',
    depends='three-js',
    resource='OrbitControls.js'
))
threejs_controls_resources.add(wr.ScriptResource(
    name='three-transformcontrols-js',
    depends='three-js',
    resource='TransformControls.js'
))


def configure_resources(settings):
    set_resource_include(settings, 'three-js', 'authenticated')
    set_resource_include(settings, 'three-objloader-js', 'authenticated')
    set_resource_include(settings, 'three-mtlloader-js', 'authenticated')
    set_resource_include(settings, 'three-acrballcontrols-js', 'authenticated')
    set_resource_include(settings, 'three-orbitcontrols-js', 'authenticated')
    set_resource_include(settings, 'three-transformcontrols-js', 'authenticated')
