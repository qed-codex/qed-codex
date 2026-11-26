---
{
  "module": "src/Formalism/LocalToGlobal/HermitianForms/TiedTwSame.lean",
  "declarations": [
    "Formalism.L2.Forms.LvSame"
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

## Twisted coordinate values and local operators

[Definition / hypothesis ARAK.D167](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.TwAtT/)

Use ([Twisted Hermitian column levels](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.TwChTied/)), ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)), ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)), ([Integral forms on column representations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.MemberForms/)) and ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)). All twisted objects below are the chosen objects of those entries. A permitted coefficient place for $Q_\mu$ means one whose rational residual characteristic $\ell_w$ belongs to none of the $F$-prime ideals in $Q_\mu$.

Hypothesis (prime-level twisting comparisons). At every source and twist choose a bijection $eV$ from twisted to untwisted finite-prime labels, with ring isomorphisms $eF_v$ of the corresponding finite fields. They identify the additive characters. Through the given initial twisting map the residue-unit actions intertwine, and the twisted initial finite form space is the image of the untwisted one. The prime-level positive integer $d^*$, positive real $D^*$ and real $\Gamma>1$ of ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)) are unchanged. At coefficient places with residual characteristic $T_u$, the recorded distinguished CM label at $v$ is the untwisted label at $eV(v)$, and the conjugate-prime flag is unchanged.

The twisted $F$-prime bijection is the composite of $eV$ with the untwisted one, and its residue ring map is $eF_v^{-1}r_{eV(v)}$. At stage $i$ its frame identification is $eY_i^{-1}$ followed by the untwisted frame identification, using the endpoint or intermediate model as appropriate.

Hypothesis (twisted coordinate presentations). For every $\mu\ne\mu_0$, $1\le i\le m$ and branch, choose a coordinate class presentation from ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)) with bad set $Q_\mu\cup\{v:v\mid g_0g_1\}$. Its base lattice, local levels, adelic level, class representatives and stabilizer matrices are exactly the rank-reindexed choices in ([Twisted Hermitian column levels](https://andrewodesky.com/rh/lean/Formalism.L2.Herm.TwChTied/)). Each branch character has finite order: some positive integer $b$ has $\chi(\kappa)^b=1$ for every level element.

At an intermediate stage its character equals the corresponding untwisted branch character on common matrices whose components in $Q_\mu$ are identity. At the terminal stage the same comparison uses the untwisted terminal character. Choose a character on the common twisted stage-$(m-1)$ Hermitian level. After reindexing it restricts to every branch coordinate character and agrees with the untwisted common character on matrices trivial at $Q_\mu$.

Require the form-space and rational-image characterizations of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)) at every nonbase positive-stage branch. Require its local integral criterion at every permitted coefficient place. Require its branch-preserving dilation conditions at these branches. At every twist, including $\mu_0$, and every $i\le m$, require the classwise normalized Fock pairing and the full embedding-dependent majorant norm identity of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)). At $\mu_0$, the chosen rational stage-zero twisting map is exactly the chosen rational untwisted coefficient identification.

For every nonbase positive-stage branch, choose all ten local reduction, kernel and distinguished-vector conditions of ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)), using the twisted class lattices and transported residue maps. Choose additive equivalences from its local level modules to the twisted finite fields. They identify the local level functional with the prescribed finite residue functional. Require the branch-preserving raising and lowering formulas and, at residual characteristic $T_u$ with true conjugate-prime flag, the mixed-basis integral criterion for the distinguished subspace $B_{w,v}$, all as stated in ([Coordinate lattices and adelic column values](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.AtTTied/)).

Hypothesis (stage-zero and base-twist operator identifications). This condition is imposed at stage zero for every twist using the chosen initial class, value and rational coefficient identifications. It is also imposed at every $i\le m$ for $\mu_0$, using the identifications induced by equality of the column chains and the prescribed rational coefficient isomorphism.

Choose additive isomorphisms from the twisted finite value modules to their untwisted counterparts, semilinear for $eF_v$, identifying their finite functionals. They carry the raising class maps to one another whenever the finite functional is $1$, and intertwine the raising operators on every function and value. Choose analogous semilinear additive isomorphisms of the finite kernel modules, preserving $t_e$. For every pair of dual functionals $g,g'$ with $$eF_v(g(x))=g'(eK_v(x)),$$ and $g\ne0$, they intertwine the lowering class maps and lowering operators on every function and value. The dilation class maps and operators intertwine under the induced map on residue-field units. At residual characteristic $T_u$ with true untwisted conjugate-prime flag, the chosen rational coefficient isomorphism identifies each distinguished $B_{w,v}$ subspace with its untwisted counterpart.

Hypothesis (common penultimate levels). Use the untwisted common local frames and symmetric subgroups $J_{N_{m-1}}^{\mathrm{false}}$ of ([Symmetric finite levels and column identifications](https://andrewodesky.com/rh/lean/Formalism.L2.Forms.FormsTiedSym/)). For every unitary lattice stabilizer element at $v\mid g_a$, membership in the common twisted stage-$(m-1)$ local level is equivalent to membership of its frame-conjugated first-component reduction in that symmetric subgroup. Outside $Q_\mu$ and $g_0g_1$, its local group equals the untwisted common group after reindexing.

For each $y\in Y_b$ choose vectors $y_G(y,a,v)\in\kappa_v^{N_{m-1}}$ for every $v\mid g_a$, equivariant for the reduced matrix action of the common level. Choose a set $Y_Q$ and a map $y_Q:Y_b\to Y_Q$. The combined maps $y_G$ and $y_Q$ separate points. Every common-level element with identity components at $Q_\mu$ fixes $y_Q$.
