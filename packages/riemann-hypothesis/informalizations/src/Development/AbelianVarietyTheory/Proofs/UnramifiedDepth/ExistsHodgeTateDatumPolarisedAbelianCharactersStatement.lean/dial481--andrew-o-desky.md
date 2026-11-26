---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsHodgeTateDatumPolarisedAbelianCharactersStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_hodgeTateDatum_polarisedAbelian_characters"
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

## Formal characters realizing an abelian Hodge–Tate matrix

[Theorem PHT.1125](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_hodgeTateDatum_polarisedAbelian_characters/)

Let $p$ be prime, $C$ algebraically closed of characteristic zero, and $v:C\to\mathbb R_{\ge0}$ a multiplicative valuation. Let $O$ be its valuation ring, a $\mathbb Z_p$-algebra complete for $(p)$, with $p$ not a unit. Let $T$ be a commutative Noetherian ring and $i:T\to O$ a ring homomorphism. Let $(A,L)/T$ be an abelian scheme of constant relative dimension $g$, equipped with a rigidified symmetric relatively ample line bundle whose translation kernel is trivial. Let $O_E$ be a commutative ring with involution acting on $A$ compatibly with the Rosati adjoint. Choose a $g$-dimensional formal group law $F$ over $T$, a nilpotent coordinate chart of $A$ for $F$, and power-series vectors $\alpha(a)\in T[[X_1,\ldots,X_g]]^g$ representing every $a\in O_E$ in that chart. There exist $c_p\in O$, a polarized Hodge–Tate datum $H$ over $O$ for $O_p=\mathbb Z_p\otimes_{\mathbb Z}O_E$ with its induced involution, and $S\in\operatorname{GL}_g(O)$ such that $$0<v(p)<1,\qquad v(c_p)^{p-1}=v(p),\qquad P_H=0,\quad P_{H,\mathrm{Lie}}=0,$$ $$d(i\alpha(a))\,S=S\rho_{H,\mathrm{Lie}}(1\otimes a)\qquad(a\in O_E).$$ Here $d$ denotes the matrix of linear terms. If $\operatorname{HT}_H\in M_{g,2g}(O)$ is the datum's Hodge–Tate matrix, then for each $1\le j\le2g$ there is $u_j\in O[[X_1,\ldots,X_g]]$ with $u_j(0)=1$, $u_j(F_O(X,Y))=u_j(X)u_j(Y)$, and $$S^t\,du_j(0)=(\operatorname{HT}_H)_{\bullet j}.$$
