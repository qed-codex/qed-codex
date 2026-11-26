---
{
  "module": "src/Formalism/LocalToGlobal/IndefiniteReal/BaseLiftsPackageOfPrimitiveLinks.lean",
  "declarations": [
    "Formalism.IndefR.Links.PrimRows3"
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

## Analytic theta maps and primitive row comparisons

[Definition / hypothesis ARAK.D213](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.ExAt/)

Use the coefficient field $K$, CM extension $E/F$, finite group $G$, tuple set $T$ with distinguished element $t_0$, and row and lifted form spaces in ([Row-side families of Hermitian spaces](https://andrewodesky.com/rh/lean/Formalism.L2.Rows.RowSideFamily/)). Use the complex realizations, measures, kernels, discrete-series models and specified linear maps in ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)). Stages $j$ run from $0$ to $m-1$. Write $\Theta_t:F_t^{\mathbb C}\to H_E$ and $\theta_{j,t}:F_{j,t}^{\mathbb C}\to H_j$ for the base and lifted theta maps. Their rational realizations are denoted $\iota_t,\iota_{j,t}$. A spectral part indexed by $p$ is denoted $H_{E,p}$ or $H_{j,p}$.

Hypothesis (existence of analytic theta maps). Use the admissibility conditions in ([Analytic theta intertwiners and Weil actions](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat.IsChainW/)), keeping all the other specified maps fixed. Require the following eight existence assertions:

1. For every $k$ with $k+1<m$, there exists an admissible tensor intertwiner $I_k$, for all tuples $t$.
2. There exists an admissible terminal tensor intertwiner $I_X$, for all $t$.
3. For every $t,k$ with $k+1<m$, there exists an admissible downward integral map $\mathcal I_{t,k}$.
4. For every $t$, there exists an admissible terminal downward integral map.
5. For every $t$, there exists an admissible base theta map $\Theta_t$.
6. For every $j$, there exists an admissible lowest-type pairing $B_j$, for all $t$.
7. For every $j,t$, there exists an admissible function-valued theta map $T_{j,t}$.
8. For every $j,t$, there exists an admissible final Hilbert-valued theta map $\theta_{j,t}$.

Hypothesis (primitive row comparisons). Impose the following conditions on the specified maps. Write $P_0,\psi_0$ and $P_1,\psi_1$ for the two level subgroups and their characters. Let $E_b\subseteq H_E$ be the selected level subspace, $W_{j,0}\subseteq H_j$ the image of the specified base-level coordinate map, and $E^{\rm pr}$ and $W_j^{\rm pr}$ the spans of the principal-level images as $t$ varies. These coordinate maps and selected rational spaces are those of ([Analytic and rational realization data](https://andrewodesky.com/rh/lean/Formalism.IndefR.Links.RealDat/)).

Every base and lifted Hecke operator has matrix coefficients in $K^{\dagger}=\{a\in K:\sigma(\bar a)=\overline{\sigma(a)}\text{ for every }\sigma:K\hookrightarrow\mathbb C\}$, and has an adjoint among its own operator family for the stabilizer-weighted class-sum pairing. The same two assertions hold for every inert operator. There exist complex Hecke operators $h^E_{t,a}$ and $h^W_{j,t,a}$ intertwining $\Theta_t$ and $\theta_{j,t}$ with the corresponding rational Hecke and inert operators; each operator family at $t_0$ is pairwise commuting. At $t_0$ the specified spaces $H_{E,p}$ and $H_{j,p}$ are exactly the sums of common generalized eigenspaces whose eigenvalues realize the indicated base type $p$ and its transported lifted type. A common generalized eigenspace for eigenvalues $(c_a)$ is $\bigcap_a\bigcup_{n\ge0}\ker(h_a-c_a)^n$.

A type is a pair of ordinary Hecke polynomials $P_p(P,X)$ and inert eigenvalues $b_p(I,\tau)$. To realize that type, an eigenvalue system $(c_{P,a},d_{I,\tau})$ satisfies $$\sum_{a=0}^n(-1)^a q_P^{a(a-1)/2}c_{P,a}X^a=P_p(P,X)\prod_{\nu\in\mathcal B}\prod_{a=0}^{t-1}(1-\nu(P)q_P^aX),\qquad d_{I,\tau}=b_p(I,\tau).$$ Here $n,q_P,t,\mathcal B$ are the recorded Hecke degree, residue cardinality, block length and block list, and prime labels are transported by their specified maps. In a complex eigensystem these rational eigenvalues are embedded through $\jmath$. The type parts sum over all systems satisfying these equalities; the lifted equalities use the specified transport of both the polynomial and inert type.

The $G$-actions on $H_E$ and every $H_j$ are unitary. They intertwine $\Theta_t\iota_t$ and $\theta_{j,t}\iota_{j,t}$ with the rational $G$-actions. Every selected rational row space is contained in its prescribed block space, on both the base and lifted sides.

There is a finite separating family of complex linear functionals $\ell_a$ on $H_E$ with $\ell_a(\Theta_t\iota_t x)\in\jmath(K)$ for every rational $x$ and $t$. For each $j$ there is such a separating family on $H_j$ for all $\theta_{j,t}\iota_{j,t}x$. A separating family on $H_j$ can also be chosen to take values in $\jmath(K)$ on every standard coordinate vector of $W_{j,0}$.

For every choice of lifted Hecke operators satisfying the intertwining, commutation and spectral-part requirements above, the following surjectivity condition holds. Let $A_j$ be the base-tuple rational good-level subspace after complexification and let $B_j=W_{j,0}$. For any common eigenvalue system $c$ occurring nontrivially in both $A_j$ and $B_j$, the full $c$-eigenspace in $A_j$ is contained in $\operatorname{im}(\theta_{j,t_0}^*)$.

Both selected row-quotient dimensions are positive. The real number $\kappa$ and every $\lambda_{j,t,p,v}$ are positive. If $H_E[P,\psi]=\{x:g x=\jmath(\psi(g))x\ (g\in P)\}$, then $$E_0=E^{\rm pr}\cap H_E[P_0,\psi_0],\qquad E_1=E^{\rm pr}\cap H_E[P_1,\psi_1].$$ Every principal-level row coordinate map is injective; all its images, including the one for $t_0$, are equal. Moreover, $$\Theta_t\Theta_t^*x=\kappa\prod_{j=0}^{m-1}\lambda_{j,t,p,v_0}\,x\quad(x\in H_{E,p}),$$ and, for each $b=0,1$, the spaces $H_{E,p}\cap E_b$ are pairwise orthogonal and span $E_b$.

At every coefficient embedding $\sigma$, the specified semilinear realization $J_{j,\sigma}$ preserves linear independence of every finite $K$-independent family and its complex span is all of $H_{j,\sigma}$. Its function realization satisfies $$J_{j,\sigma}(\rho_j(g)x)=\sigma(\chi_j(g))\,R(g)J_{j,\sigma}(x),$$ where $R(g)$ is right translation through the specified finite-level lift. The selected integral module in each $W_{j,0}$ is a full lattice. Require $$W_{j,0}=W_j^{\rm pr}\cap H_j[P_0,\psi_0^{-1}],\qquad \theta_{j,t}\theta_{j,t}^*x=\lambda_{j,t,p,v_0}x\quad(x\in H_{j,p}).$$ The spaces $H_{j,p}\cap W_{j,0}$ are pairwise orthogonal and span $W_{j,0}$.

Finally impose the following equality at every infinite place $v\ne v_0$. Let $L_{j,t_0}$ be the rational matrix of the lifted coordinate map, let $J_{j,v}$ be its realization at $v$, and let $Q_{j,t_0,v}$ be the specified Hermitian form on rational lifted coordinates. Whenever the distinguished-embedding image of $x$ belongs to $H_{j,p}$, require, for every $y$, $$\langle J_{j,v}(L_{j,t_0}x),J_{j,v}(L_{j,t_0}y)\rangle=\lambda_{j,t_0,p,v}\,Q_{j,t_0,v}(x,y).$$ For every $j,p$ require $$\dim_{\mathbb C}(H_{j,p}\cap W_{j,0})=\dim_{\mathbb C}(H_{E,p}\cap E_0).$$
