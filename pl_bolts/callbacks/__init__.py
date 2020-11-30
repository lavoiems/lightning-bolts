"""
Collection of PyTorchLightning callbacks
"""
from pl_bolts.callbacks.data_monitor import ModuleDataMonitor, TrainingDataMonitor
from pl_bolts.callbacks.printing import PrintTableMetricsCallback
from pl_bolts.callbacks.variational import LatentDimInterpolator
from pl_bolts.callbacks.vision import SRImageLoggerCallback, TensorboardGenerativeModelImageSampler
