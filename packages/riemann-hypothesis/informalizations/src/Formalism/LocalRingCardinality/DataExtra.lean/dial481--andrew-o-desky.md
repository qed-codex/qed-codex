---
{
  "module": "src/Formalism/LocalRingCardinality/DataExtra.lean",
  "declarations": [
    "Formalism.BasicNotions.Extra",
    "Formalism.BasicNotions.ExtraC"
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

## Integral and theta compatibility for families

[Definition / hypothesis ARAK.D115](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Extra/)

Hypothesis (integral and theta compatibility). For every member above the starting scale, require ([Integral level lattices and their class representatives](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ColLevel/)), ([Hermitian theta spaces and pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ThetaX/)) including Hypothesis (theta adjoints), ([Integral comparisons for theta chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.LatCmp/)), ([Twist period lattices and coefficient comparisons](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NChoice/)), ([Hermitian row lattices and their rational models](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)), ([Adjusted source lattices and explicit heights](https://andrewodesky.com/rh/lean/Formalism.MainNotions.FamP.nuDef/)), ([Local error functions and weight normalizations](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.ErrC/)), ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)), and ([Compatible adelic unitary measures](https://andrewodesky.com/rh/lean/Formalism.MainNotions.GlobalTheoryTheory.GenusMassVolumes.GaugeFam/)). All of these conditions use the same arithmetic and coefficient data, spaces, maps, local factors and constants where their symbols coincide. The shared values of constants are specified by ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)).

The remaining identifications are the following. Write $a=xe^{x^\varepsilon}$ and $f=[E:\mathbb Q]/2$. For every nonnegative integer $p$, the orbit exponent of ([Orbit weights and local loss definitions](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.Consts/)) is $$e(p)=\left\lceil C_efk^2\log_pa\right\rceil_+.$$ The coefficient $C_e$ is the real constant in ([Fixed constants in an arithmetic family](https://andrewodesky.com/rh/lean/Formalism.MainNotions.parConsts/)). At every permitted source-place pair of ([Local weight extensions and lattice chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.GatTies/)), the local lattice exponent equals $e(p_w)$. The large-prime loss function is exactly the infimum in ([Local loss from polynomial lattices](https://andrewodesky.com/rh/lean/Formalism.MainNotions.G.KapIDef/)).

At every local factor, position and stage $1\le j\le m$, the local integer filling weight is $$w_{v,j,s}=w_j(\iota_{z,w}(v,s))-\frac{k+(2j-1)(t+1)}2,$$ where $\iota_{z,w}$ is the embedding-index bijection in ([Local weight extensions and lattice chains](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.GatTies/)) and $w_j$ is the Hermitian weight. If the selected orbit set $\mathcal V_{p_w}$ is empty and $p_w\ne T_z$, require the exact localized equality $$(\widetilde N_z)_w=(M_z)_w,$$ with $\widetilde N_z,M_z$ as in ([Adjusted source lattices and explicit heights](https://andrewodesky.com/rh/lean/Formalism.MainNotions.FamP.nuDef/)).

For the initial row datum of ([Hermitian row lattices and their rational models](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)), require $\kappa_R(\iota_K)=\kappa_\sharp$, where $\kappa_R$ is the embedding-indexed coefficient in ([Divisor realizations in arithmetic families](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivX/)). Require Hypothesis (rational row lattice) in ([Hermitian row lattices and their rational models](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)) for the base finite-level row datum. Both the initial and base finite-level row data have their ambient rational models from ([Hermitian row lattices and their rational models](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.DivData/)).

The supplied constants $d_z^*$ and $D^*$ have the following exact normalizations. Let $M_E(k)$ be the standard Hermitian lattice mass in ([A common Hermitian mass constant in every positive rank](https://andrewodesky.com/rh/lean/Formalism.HermitianLattices.Ext.L3.massConst_all/)) and set $$\Delta_k(u_0,\ldots,u_{k-1})=\frac{\prod_{a<b}(u_a-u_b)}{\prod_{i=0}^{k-1}i!},\qquad U_k(\mathbb F_g)=\{A\in\mathrm{GL}_k(\mathbb F_g):A_{ii}=1,\ A_{ij}=0\ (i>j)\}.$$ Then $$d_z^*=M_E(k)\prod_{a=0}^1[\mathrm{GL}_k(\mathbb F_{g_a}):U_k(\mathbb F_{g_a})]^f\prod_{\tau\in\Sigma}\Delta_k(U^z_{\tau,0},\ldots,U^z_{\tau,k-1}).$$ For $s=m/2-1$ and $0\le i<r=k+m-1$, define $B(i)=i$ for $i<s$, $B(i)=s$ for $s\le i<s+k+1$, and $B(i)=i-k$ otherwise. Let $R_{k,m}(\mathbb F_g)$ consist of the invertible matrices with diagonal entries one, with $A_{ij}=0$ when $B(j)<B(i)$ or when $B(i)=B(j)$ and $j<i$, and with $A_{i,s+k}=0$ for $i\ne s+k$ and $B(i)=s$. Require $$D^*=\operatorname{vol}(Y_0)\prod_{a=0}^1[\mathrm{GL}_r(\mathbb F_{g_a}):R_{k,m}(\mathbb F_{g_a})]^f\prod_{\tau\in\Sigma}d_\tau.$$ Here $\operatorname{vol}(Y_0)$ is the specified positive volume assignment and $d_\tau>0$ are the specified positive scalars in ([Identifications for arithmetic family members](https://andrewodesky.com/rh/lean/Formalism.MainNotions.N.LocTie/)). The weights $U^z$ are those in ([Column chains and period pairings](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.Member/)).
