---
{
  "module": "src/Formalism/LocalRingCardinality/DataKerP.lean",
  "declarations": [
    "Formalism.BasicNotions.LocalToGlobal₂",
    "Formalism.BasicNotions.TwForms"
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

## Integral comparisons for theta chains

[Definition / hypothesis ARAK.D114](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)

Hypothesis (integral chain comparisons). Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)), ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)), ([Complex vector spaces and integral spans](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Rows.Data/)), and ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)). Write $K$ for the coefficient field, $z$ for a source, $\mu$ for a twist, $V_{z,\mu,j}$ for the rational coefficient space at stage $j$, $M_{z,\mu,j}$ for its integral lattice, and $J_{z,\mu,j}$ for its semilinear complex realization.

For every $z,\mu$, choose twisted prime-level data and integral coefficient forms satisfying ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)) and ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)), with prime $T_z$. There is a $K$-linear isomorphism $a_{z,\mu}:V_{z,\mu_0,0}\simeq V_{z,\mu,0}$ carrying $M_{z,\mu_0,0}$ onto $M_{z,\mu,0}$, and its complex realization is the specified initial twist isomorphism. For the distinguished twist $\mu_0$ and every $j\le m$, choose $K$-linear isomorphisms from the original stage spaces to these twisted-model stage spaces, preserving their integral lattices and agreeing with the original complex realization after identifying the base chains.

Call $(z,w)$ eligible when $p=p_w\ge5$ is in the inert prime class, has cyclic Frobenius coordinate of even order at every prime above it, is outside the level-prime set and does not divide $T_z$. For every eligible pair choose an embedding $\jmath_{z,w}:K\to F_{z,w}$ into the local coefficient field, inducing $w$: $$v_w(a)\ge0\quad\Longleftrightarrow\quad\jmath_{z,w}(a)\in R_{z,w},$$ where $R_{z,w}$ is the local DVR. There is a $\jmath_{z,w}$-semilinear map $c_{z,w}:V_{z,\mu_0,0}\to\mathcal F_{z,w,0}$ into the local function space. Images of the specified rational basis are linearly independent over $F_{z,w}$ and the $R_{z,w}$-span of $c_{z,w}(M_{z,\mu_0,0})$ equals the specified local lattice $M$.

The specified local ramified submodule, viewed as a set, equals the $F_{z,w}$-span of the image of the rational ramified subspace. If the selected orbit set $\mathcal V_p$ is nonempty, require $$x\in(\widetilde N_z)_w\quad\Longleftrightarrow\quad c_{z,w}(\nu_zx)\in N_p,$$ where $\nu_z$ is the rational source injection and $N_p$ is defined below. At $p_w=T_z$, instead require $$x\in(\widetilde N_z)_w\quad\Longleftrightarrow\quad\nu_zx\in T_z^{m\sum_{v\in V_{z,w}}b_{\tau_{w,v}}}\,\left(\prod_{v\in V_{z,w}}U_v\right)^m\left((M_{z,\mu_0,0})_w\cap V^{\rm ram}_{z,0}\right).$$ Here $V_{z,w}$ is empty if the Boolean level flag is false, and otherwise consists of those selected level labels whose assigned embedding is in $\Sigma_{\rm top}$. The operators $U_v$ sum the class-raising coefficient operators over the finite residue vectors for which the selected residue functional equals one, and the product is taken in the specified finite-list order; these operators and functionals are those of ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)). Images in this formula are taken through the rational realization: a rational vector is included exactly when its complex image is obtained by the displayed operator.

For every eligible pair there is an embedding $\lambda:\overline{\mathbb Q}\cap\mathbb C\to\mathbb C_p$ and an embedding $F_{z,w}\to\mathbb C_p$ agreeing with $\lambda$ on the complex image of $K$. The local filling has increment $t$ and $m$ stages. For every stage and local factor $v$, choose an embedding $E\to Q_{j,v}$. For each local component $a$ and local lattice tuple $L$, choose an $\mathcal O_E$-submodule $\Gamma_{j,a,L}\subseteq E^{N_j}$. For $j\le m$ and genuine lattice tuples, its span through $E\to Q_{j,v}$ is exactly $L_v$.

Choose a class label $c(j,a,L)$ in the global twisted chain. For $j\le m$ and genuine tuples, $$c(j,a,L)=c(j,a',L')\quad\Longleftrightarrow\quad a=a'\text{ and }L'=\gamma L\text{ for some }\gamma\in\Gamma_{j,a}^{\rm loc}.$$ Here $\Gamma_{j,a}^{\rm loc}$ is the local arithmetic subgroup in ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)). Every global twisted class at these stages is obtained from some $a,L$. For every adjacent pair $(a,L),(a',L')$, choose a formal power series over $\mathbb C_p$ in variables indexed by $\Sigma\times\{1,\ldots,N_{j+1}\}\times\{1,\ldots,N_j\}$.

For every $j$ there is a semilinear comparison $C_j:V_{z,\mu_w,j}\to\mathcal F_{z,w,j}$; it is injective for $j\le m$. At $j=0$ it agrees with $c_{z,w}$ after $a_{z,\mu_w}$, and the $R_{z,w}$-span of its integral image is the local integral module. For $j<m$, if two rational vectors have complex images related by the global transition $K_j$, their comparison images are related by the specified local transition $K_j^{\rm loc}$.
