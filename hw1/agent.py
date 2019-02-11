#DotDict
class DotDict(dict):
    def _getattr_(self, name):
        return self[name]

#Pass Arguments
args = DotDict({
    'batch_size' : 128,
    'epochs' : 50,
    'envname' : 'Hopper-v1',
    'expert_policy_file' : 'experts/Hopper-v1.pkl',
    'num_rollouts' : 5,
    'render' : False,
    'max_timesteps' : 300,
    'verbose' : 1,
})

#Generate plot
def gen_new_plot(title, ylabel, xlabel):
    fig, ax = plt.subplots(nrows = 1, ncols = 1)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    return ax

# Suppress Tensorflow warning complaining about not using certain instruction sets
# Arises when not install tensorflow from source
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


