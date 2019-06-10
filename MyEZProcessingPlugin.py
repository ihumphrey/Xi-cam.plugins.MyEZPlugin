from xicam.plugins.ProcessingPlugin import EZProcessingPlugin

def increase(x, y, z):
    x += 10
    y += 10
    z += 1


increase_plugin = EZProcessingPlugin(increase)
print('-'*80)
print(increase_plugin)
print(f'increaseplugin __dict__:\n\t{increase_plugin.__dict__}')
print(f'increaseplugin __dict__.items():\n\t{increase_plugin.__dict__.items()}')
print('evaluating...')
increase_plugin()
print('...done')
print(f'increaseplugin __dict__:\n\t{increase_plugin.__dict__}')
print(f'increaseplugin __dict__.items():\n\t{increase_plugin.__dict__.items()}')
print()
exit(1)