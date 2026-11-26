---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SphericalSectionGraphSplitPlaceStatement.lean",
  "declarations": [
    "GlobalTheory.T.sphericalSection_graph_splitPlace"
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

## A spherical section evaluated on a split doubling graph

[Theorem AGR.0821](https://andrewodesky.com/rh/lean/GlobalTheory.T.sphericalSection_graph_splitPlace/)

Fix the source's full CM unitary arithmetic datum with fields $E/F$. Let $A$ be a based Hermitian space of rank $n$, $L$ a full self-dual $\mathcal O_E$-lattice, $\chi:\mathbb A_E^\times\to S^1$ a group character, and $b\ge0$. Assume the restriction condition below. Let $v$ split in $E/F$, and assume $\chi$ is unramified at every $w\mid v$.

Let $s\in\mathbb C$ and let $\phi$ be a normalized spherical section of the degenerate principal series on $U(A\oplus(-A))(F_v)$ induced by $\chi_v^{-1}$ with exponent $s+n/2$. Choose $w\mid v$ and a split identification $e:U(A)(F_v)\simeq\operatorname{GL}_n(E_w)$ obtained from a basis of $L_w$ and carrying its stabilizer to $K=\operatorname{GL}_n(\mathcal O_{E_w})$. Let $\varpi$ be a uniformizer, $q_w=|\mathcal O_E/w|$, and $d\in\mathbb Z^n$. Put $t=\operatorname{diag}(\varpi^{d_1},\ldots,\varpi^{d_n})$. For $k_1,k_2\in K$, $$\phi\bigl(\operatorname{diag}(e^{-1}(k_1tk_2),1)\bigr) =\chi_w(\varpi)^{-\sum_i d_i}\,q_w^{-(n/2+s)\sum_i|d_i|}.$$
