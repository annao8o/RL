import sys, os, random
import numpy as np
import pandas as pd

class DataLoader(object):
    def __init__(self):
        self.requests = []
        self.operations = []

    def get_requests(self):
        pass
    def get_operations(self):
        pass

class DataLoaderZipf(DataLoader):
    def __init__(self, num_files, num_samples, param, num_progs=1, operation='random'):
        super(DataLoaderZipf, self).__init__()

        for i in range(num_progs):
            files = np.arange(num_files)
            #Random ranks
            ranks = np.random.permutation(files) + 1
            #Distribution
            pdf = 1 / np.power(ranks, param)
            pdf /= np.sum(pdf)

            self.requests += np.random.choice(files, size=num_samples, p=pdf).tolist()
            if operation == 'random':
                self.operations += np.random.choice([0,1], size=num_samples).tolist()
            else:
                self.operations += np.full(num_samples, int(operation)).tolist()

    def get_requests(self):
        return self.requests

    def get_operations(self):
        return self.operations


# class DataLoaderPintos(DataLoader):
#     def __init__(self, progs, boot=False):
#         super(DataLoaderPintos, self).__init__()
#
#         if isinstance(progs, str):
#             progs = [progs]
#
#         for prog in progs:
#             df = pd.read_csv(prog, header=0)
#             if not boot:
#                 df = df.loc[df['boot/exec'] == 1, :]
#                 self.requests += list(df['blocksector'])
#                 self.operations += list(df['read/write'])
#
#     def get_requests(self):
#         return self.requests
#
#     def get_operations(self):
#         return self.operations




# if __name__ == "__main__":
#
#     if len(sys.argv) != 6:
#         print("Usage: %s <save_path> <num_resources> <num_samples> <zipf_param> <num_progs>" % sys.argv[0])
#         exit(0)
#
#     save_path = sys.argv[1]
#     num_files = int(sys.argv[2])
#     num_samples = int(sys.argv[3])
#     param = float(sys.argv[4])
#     num_progs = int(sys.argv[5])
#
#     df = None
#     for i in range(num_progs):
#         files = np.arange(num_files)
#         # Random ranks. Note that it starts from 1.
#         ranks = np.random.permutation(files) + 1
#
#         # Distribution
#         pdf = 1 / np.power(ranks, param)
#         pdf /= np.sum(pdf)
#
#         # Draw samples
#         requests = np.random.choice(files, size=num_samples, p=pdf)
#         operations = np.full_like(requests, 0)
#         executions = np.full_like(requests, 1)
#
#         # Make dataframe and save .csv
#         tmp = pd.DataFrame({'blocksector': requests, 'read/write': operations, 'boot/exec': executions})
#         if df is None:
#             df = tmp
#         else:
#             df = pd.concat((df, tmp), axis=0)
#     # Save
#     df.to_csv(save_path, index=False, header=True)

