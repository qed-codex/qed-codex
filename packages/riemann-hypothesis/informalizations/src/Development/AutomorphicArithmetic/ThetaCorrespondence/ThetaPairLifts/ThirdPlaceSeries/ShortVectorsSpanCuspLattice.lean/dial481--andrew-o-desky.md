---
{
  "module": "src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ShortVectorsSpanCuspLattice.lean",
  "declarations": [
    "GlobalTheory.T.short_vectors_span_cusp_lattice_alt"
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

## Uniformly short sections spanning the prescribed cusp space

[Theorem ARAK.1358](https://andrewodesky.com/rh/lean/GlobalTheory.T.short_vectors_span_cusp_lattice_alt/)

Assume the source's published Hodge-bundle input theorems and its three global conditions on auxiliary families: goodness of the deeper covers, the size condition, and the flat-degree condition. Work in the source's full family of arithmetic auxiliary points, satisfying its family hypotheses and its pointwise compatibility and recursive-tie conditions. A cover means a deeper finite-level moduli cover with its integral cusp lattice and its comparison to the Hermitian automorphic model; retain the source's good-cover conditions.

There is $\varepsilon_0>0$ such that, for every $0<\varepsilon\le\varepsilon_0$, there are source-family threshold rules with this property: for every family and real construction constant $C_H$ satisfying the full family hypotheses and these threshold rules, there are $C\ge0$ and a scale threshold such that, at every larger scale above the family's starting scale, for every allowed point, every stage $i$ with $i+1<m$, every good cover $Y$, and every component $Z$ of that cover, there are finitely many vectors $v_1,\ldots,v_h$ in its prescribed integral cusp lattice of weight $\lambda$ satisfying $$\operatorname{span}_F\{v_1,\ldots,v_h\}=V_\lambda(Z),\qquad \|v_j\|_{\sigma,\mathrm{Pet}}\le\exp\!\left(dP\left(\frac{K}{T}+1\right)\right)$$ for every $j$ and every embedding $\sigma:F\to\mathbb C$ of the cover's coefficient field. Here $V_\lambda(Z)$ is its cusp-form space, $d$ is the flag dimension, $P$ is the family's specified real size parameter, $K$ is the sum of the absolute values of the original integral weight coordinates, and $$T=\left\lceil P^2d^2\frac{k}{m}\right\rceil_{\!\mathbb N}.$$ Here is the weight construction, performed separately at each CM embedding. Let $A=(A_j)_{0\le j<p+q}$ be the original integral weight; subtract its coordinate at index $k-2$ from every coordinate, taking the subtracted value as zero if that index is out of range, and call the result $u$. Let $f=[E:\mathbb Q]/2$, let $r$ be the Hermitian rank in the arithmetic datum, and let $c_0$ be the least nonnegative multiple of eight at least $\max\{r+\binom{fpq+1}{2}+2,8fr+4\}$. Set $h_j=0$ for $j<p$ and $h_j=-1$ for $j\ge p$, and set $\kappa_j=q+2(j+1)-p-1$ for $j<p$ and $\kappa_j=-p+2(j-p+1)-q-1$ otherwise. Put $b=u-c_0h-\kappa$, $a=k-2$ with truncated natural subtraction, and $N=T+d+1$. For the adjacent gaps $g_j=b_j-b_{j+1}$, extended by zero outside their range, put $q_j=g_j\mathbin{\mathrm{div}}N$, $r_j=g_j-Nq_j$, where $\mathrm{div}$ is Euclidean integer division. Define $Q_j=\sum_{t<a}q_t-\sum_{t<j}q_t$ and $R_j=\sum_{t<a}r_t-\sum_{t<j}r_t$. The required weight is $\lambda_j=\kappa_j+(d+1)Q_j+R_j$. The quantities $k,m$ are respectively the auxiliary rank parameter and number of stages in the full arithmetic datum, and $\lceil\ \rceil_{\mathbb N}$ is the nonnegative ceiling.
