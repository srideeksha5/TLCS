from tensorflow.keras.models import load_model
from tensorflow.keras.utils import plot_model
import os

model = load_model(r"C:\Users\srinivasulu\Documents\Deep-QLearning-Agent-for-Traffic-Signal-Control\TLCS\models\model_9\trained_model.h5")

plot_model(model, to_file=os.path.join(r'C:\Users\srinivasulu\Documents\Deep-QLearning-Agent-for-Traffic-Signal-Control\TLCS\models\model_9', 'model_structure.png'), show_shapes=True, show_layer_names=True)
