import json
import os
from time import time
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import optparse
import zipfile
try:
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D # used for 3D plotting
except ImportWarning:
    print('Could not import matplotlib - plots won\'t be created')

# assumes that the package was installed in currently used environment
from calcbsimpvol import calcbsimpvol


def scatter3d(x, y, z, x_label=None, y_label=None, z_label=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_zlabel(z_label)

    plt.show()
    return


def scatter2d(x, y, x_key=None, y_key=None, x_label=None, y_label=None):
    """convenience"""

    if x_label is None:
        x_label = x_key
    if y_label is None:
        y_label = y_key

    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(x, y)
    box = [ax.get_ylim()[0], ax.get_ylim()[1], ax.get_xlim()[0], ax.get_xlim()[1]]
    new_size = [np.min(box), np.max(box)]
    ax.plot(new_size, new_size,)
    ax.set_xlim(new_size)
    ax.set_ylim(new_size)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    plt.show()


def load_data(file_path):
    with zipfile.ZipFile(file_path, 'r') as zf:
        file_names = zf.namelist()
        if len(file_names) != 1:
            raise ValueError('expected archive to have only one file')
        if file_names[0] not in file_path:
            raise ValueError('expected file name to be part of the archive name')
        data_string = zf.read(file_names[0])
        return data_string


def calc(file_path, steps=1, do_return=False):
    data_string = load_data(file_path)
    data = json.loads(data_string)
    container = dict()
    for day in data:
        m = data[day]
        c = dict()
        c['cp'] = np.asarray(m['cp'])
        c['P'] = np.asarray(m['P'])
        c['S'] = np.asarray(m['S'][0])
        c['K'] = np.asarray(m['K'])
        c['tau'] = np.asarray(m['tau'])
        c['r'] = np.asarray(m['r'])
        c['q'] = np.asarray(m['q'])

        feed_keys = ['cp', 'P', 'K', 'tau', 'r', 'q']
        for key in feed_keys:
            c[key] = np.reshape(c[key], (np.size(c[key]), 1))
            container[day] = c.copy()

    elapsed = dict()
    array_size = dict()

    for _step in range(steps):
        elapsed[_step] = dict()
        array_size[_step] = dict()
        for day in container:
            t_zero = time()
            if _step == 0:
                container[day]['py_rational'] = calcbsimpvol(container[day])
            else:
                calcbsimpvol(container[day])
            elapsed[_step][day] = time() - t_zero
            array_size[_step][day] = np.size(container[day]['cp'])

    _days = len(container.keys())
    _options_per_step = np.sum([array_size[0][day] for day in array_size[0]])
    _average_options_per_day = _options_per_step/_days
    _total_elapsed_array = [0] * steps
    for _step in range(steps):
        _total_elapsed_array[_step] = np.sum([elapsed[_step][day] for day in elapsed[_step]])

    _total_elapsed = np.sum(_total_elapsed_array)
    _min = np.min(_total_elapsed_array)  # s

    print('steps {}'.format(steps))
    print('days per step: {}'.format(_days))
    print('total elapsed time: {} ms'.format(np.round(_total_elapsed * 1000)))
    print('total options: {} '.format(_options_per_step * steps))
    print('(best) average time per option: {} µs'.format(np.round((_min / _options_per_step) * 1000 * 1000 )))
    print('')
    print('options per step: {}'.format(_options_per_step))
    print('minimum elapsed time for 1 step: {} ms'.format(np.round(_min * 1000)))
    print('')
    print('average time per option: {} µs'.format(np.round((_total_elapsed/(steps * _options_per_step)) * 1000 * 1000)))
    if do_return:
        return container


def main(file_path, steps):
    results = calc(file_path=file_path, steps=steps, do_return=True)
    reference_data = json.loads(load_data(file_path))

    # 'reference' sample has only one single day (complete surface)
    # but 'cl' and 'spy' have multiple days for a single expiry
    if p.mode == 'reference':
        day_to_plot = (list(results.keys()))[0]  # there is one day of data
    else:
        day_to_plot = (list(results.keys()))[5]  # pick a day =)

    if p.mode == 'reference':
        selector = reference_data[day_to_plot]['cp'] == np.asarray(1)  # compare only calls, `-1` for puts
        try:
            scatter2d(x=np.asarray(reference_data[day_to_plot]['ref_iv_clean'])[selector],
                      y=np.asarray(results[day_to_plot]['py_rational'])[selector],
                      x_key='ref_iv_clean',
                      y_key='py_rational')
        except NameError:
            print('Skipping plot part - could not executes `scatter2d` in example3.')
        m = np.log(results[day_to_plot]['S'] / results[day_to_plot]['K'])
        try:
            scatter3d(x=m,
                      y=results[day_to_plot]['tau'],
                      z=results[day_to_plot]['py_rational'],
                      x_label='log(F/K)', y_label='tau = T - t_0', z_label='sigma')
        except NameError:
            print('Skipping plot part - could not executes `scatter3d` in example3.')

    # next plot is note supposed to be used for quality measurement
    # it was simply a way to check visually whether the Python translation correlates
    # with the MATLAB implementation
    else:
        try:
            scatter2d(x=reference_data[day_to_plot]['mlb_rational'],
                      y=results[day_to_plot]['py_rational'],
                      x_key='mlb_rational',
                      y_key='py_rational')
        except NameError:
            print('Skipping plot part - could not executes `scatter3d` in example3.')


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option(
        '-m', '--mode',
        action='store',
        dest='mode',
        help='select a mode to run a test with the included data. ie: spy ',
        default='reference'
    )

    parser.add_option(
        '-s', '--steps',
        action='store', dest='steps',
        help='run it how often? default: 100',
        default=100,
        type=int
    )
    p, args = parser.parse_args()
    if p.mode == 'reference':
        file_path = os.path.join('..', 'data', 'reference_sample.json.zip')
    # these have reference data, however the data is not from a third party
    elif p.mode == 'spy':
        file_path = os.path.join('..', 'data', 'spy_20190118.json.zip')
    elif p.mode == 'cl':
        file_path = os.path.join('..', 'data', 'cl_20171115.json.zip')
    else:
        raise ValueError('must be run with an argument (`reference`, `spy`, `cl`)')

    main(file_path=file_path, steps=p.steps)
