from azureml.core import Workspace
from azureml.core.model import Model


# Create Workspace
ws = Workspace.create(name = 'deployed_agrix_nn', subscription_id = '94309b5e-965a-4b8c-850a-95a8824ee3a7', create_resource_group = True, location = 'westeurope')
# Register model with workspace
model = Model.register(model_path = '../trained_models/some_agrix_nn.h5', model_name = 'Predictor', description = 'Some NN trained on diseased crops', workspace = ws)