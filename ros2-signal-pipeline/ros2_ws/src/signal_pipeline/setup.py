from setuptools import setup
package_name='signal_pipeline'
setup(
  name=package_name, version='0.0.1', packages=[package_name],
  data_files=[
    ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/pipeline.launch.py']),
  ],
  install_requires=['setuptools'], zip_safe=True,
  maintainer='Ram', maintainer_email='ram@example.com',
  description='Minimal sine->RMS pipeline for November', license='MIT',
  entry_points={'console_scripts':[
    'signal_pub=signal_pipeline.signal_pub:main',
    'rms_sub=signal_pipeline.rms_sub:main',
    'analyze_bag=signal_pipeline.analyze_bag:main',
  ]},
)
