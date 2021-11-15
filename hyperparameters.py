from tensorflow import keras

parameters = {'name': 'test_3',
              'epochs': 20,
              'batch_size': 32,
              'img_dim': 128,
              'latent_dim': 256,
              'beta': 1.0,
              'initial_learning_rate': 0.0001,
              'demo_iterations': 100,
              'validation_frequency': 1 / 100,
              'monitoring_frequency': 1 / 1000
              }

parameters['learning_rate'] = keras.optimizers.schedules.ExponentialDecay(
    parameters['initial_learning_rate'],
    decay_steps=2500,
    decay_rate=0.96,
    staircase=True)
