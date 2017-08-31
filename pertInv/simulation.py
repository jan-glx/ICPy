import numpy as np

n_genes = 200
n_guides = 10
n_cells = 1000

gene_log_expression_scale = np.random.normal(loc=-2, scale=2, size=n_genes)
log_exposure = np.random.normal(scale=0.5, size=n_cells)
background = np.random.normal(scale=1 / np.sqrt(n_genes), size=(n_cells, n_genes))

B = np.random.normal(scale=4 / np.sqrt(n_genes), size=(n_genes, n_genes)) *  np.random.binomial(n=1, p=10/n_genes, size=(n_genes, n_genes)) #np.random.laplace(scale=5 / n_genes, size=(n_genes, n_genes))
di = np.diag_indices(n_genes)
B[di] = 0#-np.abs(B[di]) - 0.1

guide_abundance = np.random.lognormal(sigma=0.2, size=n_guides)
guide_efficacy = np.random.beta(a=6, b=3, size=n_guides)
guide_effects = np.random.randint(n_genes, size=n_guides)


def zero_truncated_multipoisson(lam, size):
    lam = np.array(lam, ndmin=1)
    # adapted from Ted Harding (https://stat.ethz.ch/pipermail/r-help/2005-May/070678.html)
    n = size  # desired size of sample
    T = np.sum(lam)  # pre-truncation mean of Poisson
    U = np.random.uniform(size=n)  # the uniform sample
    t = -np.log(1 - U * (1 - np.exp(-T)))  # the "first" event-times
    T1 = (T - t)  # the set of (T-t)
    X = np.random.poisson((lam[np.newaxis, :] * T1[:, np.newaxis] / T))
    first = np.random.multinomial(1, lam / sum(lam), size=n)
    X += first
    return X


guide_matrix = zero_truncated_multipoisson(guide_abundance, size=n_cells)
knockout_matrix = np.random.binomial(n=1, p=1 - (1 - guide_efficacy) ** guide_matrix)
guide_matrix = guide_matrix > 0

environment, o2s, s2o, count = np.unique(guide_matrix, axis=0, return_index=True, return_inverse=True,
                                         return_counts=True)
start_stops = np.hstack([[0], np.cumsum(count)])

I = np.identity(B.shape[0])
Z = np.zeros(shape=(n_cells, n_genes))
for e in range(len(count)):
    # Z=Z B + background
    # Z (B-I) = -background
    # (B-I).T Z.T = -background.T
    cells_e = s2o[start_stops[e]:start_stops[e + 1]]
    background_e = background[cells_e]
    B_e = B
    B_e[guide_effects[environment[e]]] = 0
    Z_e = np.linalg.lstsq((B_e - I).T, -background_e.T)[0].T
    assert (np.allclose(Z_e, np.matmul(Z_e, B_e) + background_e))
    Z[cells_e] = Z_e
Z += gene_log_expression_scale[np.newaxis, :]

np.set_printoptions(linewidth=200)
print(np.histogram(Z))
count_matrix = np.random.poisson(np.exp(Z + log_exposure[:, np.newaxis]))

print(count_matrix)

print(np.mean(count_matrix))
print(np.std(count_matrix))
# print(np.histogram(count_matrix))
print(np.std(np.mean(count_matrix, axis=0)))  # mean of genes
print(np.std(np.mean(count_matrix, axis=1)))  # mean of cells
print(np.std(np.corrcoef(count_matrix)))