---
{
  "module": "src/Formalism/LocalToGlobal/LatticeGeometry/ShimuraSheafOfIndefiniteSubspace.lean",
  "declarations": [
    "Formalism.L2.Geo.CompatibleGeometry",
    "Formalism.L2.Geo.CompatibleLevelPrimes",
    "Formalism.L2.Geo.CompatiblePlaces'",
    "Formalism.L2.Geo.TiedX"
  ],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Geometric realization and level compatibility

[Definition / hypothesis ARAK.D175](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.GeoTiedP/)

Hypothesis (geometric realization and level compatibility). Use ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)), with its level set $\mathcal K$, divisor operations, selected-stage varieties, integral section spaces, and local model data. There is a choice of all data in ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)), ([Integral charts and theta representations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.CF/)), ([Extensions of integral charts and degree filtrations](https://andrewodesky.com/rh/lean/Formalism.MainNotions.ModuliIntegralCharts.ExtA/)), ([Boundary characters and integral Fourier jets](https://andrewodesky.com/rh/lean/Formalism.MainNotions.BoundaryLocalData.LocB/)), and ([Cuspidal sections and their integral Fourier data](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)), satisfying the following identifications.

Choose a finite prime set $S_\kappa$ for every $\kappa\in\mathcal K$ and a distinguished $\kappa_g$ such that $S_{\kappa_g}=\{g_0,g_1\}$. Choose the embeddings $\jmath_{p,\mathfrak l}$ and the auxiliary sets $\mathcal N_g,\mathcal F_{g,c}$ once, and a geometric model for every geometric input $(S,\kappa,j)$ of ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)). The stage-$a$ input used for the cuspidal section data, for every $a\ge0$, is $$S=W_{a'},\qquad\kappa=\kappa_g,\qquad j=(\operatorname{sig}W_{a'})_+,\qquad a'=\max(1,\min(a,m)).$$ Its rank is the specified common rank $r$ of the spaces $W_a$. Its component, divisor and chart-point data are precisely those used for $S_{a,w}$ and the Fourier data in ([Cuspidal sections and their integral Fourier data](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.FormsPkg/)).

For every prime $p$, choose a bijection from the given local-place set to the finite coefficient places $\mathfrak l\mid p$. For every $1\le a\le m$, choose a bijection from the given stage-$a$ component set to the component set of the geometric model at $(W_a,\kappa_g,(\operatorname{sig}W_a)_+)$. Under these bijections the following equalities are required.

The given level-prime assignment is exactly $\kappa\mapsto S_\kappa$. For every geometric input $(S,\kappa,j)$ with $1\le j<N$, its given geometric datum equals the datum constructed from ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)): the rank, signature index, level primes, components, total volume, degree functional, arithmetic degree and mixed-degree functionals, both curve sets and their degrees, fiber components and boundary predicate, point set and its three numerical functions, complex quotient and its numerical functions, component maps, determinant functions, and arithmetic line data with all their component and total functions and predicates are exactly the constructions specified there. In particular the complex degree functional is $(\sum_cv_c)\deg_{\rm fl}$, and the total arithmetic and geometric degrees are sums of their component values. This is equality of the specified data, with their indicated coordinate identifications.

At $\mathfrak l\mid p$ the given place weight and embedding equal $$\frac{e_{\mathfrak l}\log\mathrm N\mathfrak l}{[K:\mathbb Q]\log p},\qquad\jmath_{p,\mathfrak l},$$ where $e_{\mathfrak l}$ is the absolute ramification index. For every indefinite geometric input, the given local model set, reduction intersection datum, curve sets, degree functions and distinguished Hodge models are the ones in ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)) at the matched place. The given identification of a Hodge curve with a place and a curve at its distinguished Hodge model agrees with the disjoint-union identification there: every identified pair of Hodge curves has the same place under the chosen place bijection and the same curve after transport. For $1\le a\le m$, the given component varieties, boundary labels and weight-divisor maps agree, under the component bijection, with $Y_{a,c},B_{a,c},L_{a,c}$. Equality of weight-divisor maps is required for every integer weight array of length $r$.

For every prime $p$, place $\mathfrak l\mid p$, embeddings $\tau:E\to\mathbb K_p$ and $e:E\to K$ with $\jmath_{p,\mathfrak l}\tau=\iota_\infty e$, and every $x\in\mathcal O_E$, require $$\tau(x)\in\{b\in W(\overline{\mathbb F}_p):b_0=0\}\ \Longleftrightarrow\ |e(x)|_{\mathfrak l}<1.$$ The Witt vectors on the left are viewed in their fraction field, and $b_0$ is their zeroth Witt coordinate.

For every $1\le a\le m$, every given stage component $c$, and every vector $x$ in the rational space underlying the given Hermitian section datum, its image section vanishes on the specified boundary of that component at the specified weight divisor $L_{a,c}(\kappa_a)$.

If two geometric inputs have the same level and signature index and there is an $E$-linear isometry between their Hermitian spaces carrying the specified lattice onto the specified lattice, then, whenever both inputs are indefinite, the constructed geometric data are equal. Finally the predicate $I(M)$ of ([Complex and integral geometric models](https://andrewodesky.com/rh/lean/Formalism.L2.Geo.Dat/)) agrees with the prescribed level-membership predicate for every geometric input and every $M\ge0$; its dependence on the input is exactly through that input's level $\kappa$.
