from azureml.core.image import ContainerImage
from azureml.core.model import Model
from azureml.core.webservice import Webservice
from azureml.core import Workspace

from keras.models import load_model


ws = Workspace.create(name = 'deployed_agrix_nn', subscription_id = '94309b5e-965a-4b8c-850a-95a8824ee3a7', create_resource_group = True, location = 'westeurope')


model_path = Model.get_model_path(model_name = 'Predictor')
model = load_model(model_path)

image_config = ContainerImage.image_configuration(execution_script = "score.py", runtime = "python",conda_file = "myenv.yml",description = "Environment definitions")

service = Webservice.deploy_from_model(workspace=ws, name='Agrix-Predictions', models=[model], image_config=image_config)

service.wait_for_deployment(show_output=True)

print(service.scoring_uri)