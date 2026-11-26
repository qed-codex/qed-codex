---
{
  "module": "src/Development/WeilBound/ThetaLifts/LatticeBasics/HypothesesS.lean",
  "declarations": [
    "GlobalTheory.ThK.Dbl.SiegelWeilStd"
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

## Hypothesis: the Siegel-Weil formula on the doubled group for a definite space, with constant 1 or 2

[Definition / hypothesis THETA.D085](https://andrewodesky.com/rh/lean/GlobalTheory.ThK.Dbl.SiegelWeilStd/)

The hypothesis of this page concerns an Eisenstein sum on a doubled group that is formed from a Schwartz function: the value of its meromorphic continuation at one point is $1$ or $2$ times an average of theta functions over the unitary group of a definite space. The adele rings $\mathbb A$ and $\mathbb A_E$, the absolute value $|\cdot|_{\mathbb A}$ on $\mathbb A^\times$, admissible base data with their additive character $\psi$, Hermitian and skew-Hermitian data and their signatures, the groups $U(A)(\mathbb A)\supset U(A)(F)$, the space $\mathcal S(\mathbb A^\kappa)$ of Schwartz functions, tempered linear functionals, regular homomorphisms and the theta sum $\theta$ are those of ([Setting for theta lifts between unitary groups of a CM extension: base data, Hermitian data, Weil representations, theta integrals](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Base.IsGood/)). The doubled group $G$ with its matrix $\tilde J_Y$, the matrix $\Delta$, the Siegel parabolic subgroup $\mathcal P$ with the matrices $t_p$, frames, standard compact subgroups, height functions, Eisenstein sums, Hecke characters and the function $\eta$ are defined in ([Siegel Eisenstein sums on the doubled group of a Hermitian datum: frames, standard compact subgroups, height functions, sections](https://andrewodesky.com/rh/lean/GlobalTheory.ThK.Dbl.G2/)).

**The two spaces.** Let $F$ and $E$ be number fields, $E$ an $F$-algebra, and $\sigma\colon E\to E$ a homomorphism of $F$-algebras, and let base data admissible for $\sigma$ be given. Let $m,n\ge1$ be integers, and let $A$ and $Y$ be Hermitian data of dimensions $m$ and $n$, with matrices $J_A$ and $J_Y$, such that

- either $A$ is Hermitian and $Y$ is skew-Hermitian, or $A$ is skew-Hermitian and $Y$ is Hermitian;
- the signature of $A$ is $(m,0)$ or $(0,m)$, and the signature of $Y$ is arbitrary.

Let $G$ be the doubled group of $Y$, and let $\chi$ be a Hecke character whose restriction to $\mathbb A^\times$ is $\eta^m$.

**Coordinates and Heisenberg operators.** Let $\kappa$ be a finite set and $\mathbb W=M_{m\times2n}(\mathbb A_E)$. For $x,y\in\mathbb W$ put $$\langle\!\langle x,y\rangle\!\rangle=-\mathrm{Tr}_{\mathbb A_E/\mathbb A}\sum_{i,j,k,l}x_{ij}\,(J_A)_{ik}\,(\tilde J_Y)_{jl}\,\sigma(y_{kl}),$$ where $\tilde J_Y=\mathrm{diag}(J_Y,-J_Y)$. *Coordinates on $\mathbb W$ indexed by $\kappa$* are an $\mathbb A$-linear isomorphism $\tilde e=(\tilde e_1,\tilde e_2)\colon\mathbb W\to\mathbb A^\kappa\times\mathbb A^\kappa$ such that $$\langle\!\langle x,y\rangle\!\rangle=\tilde e_1(x)\cdot\tilde e_2(y)-\tilde e_1(y)\cdot\tilde e_2(x)\qquad(x,y\in\mathbb W).$$ Given such coordinates, the Heisenberg operator of $w\in\mathbb W$ acts on functions on $\mathbb A^\kappa$ by $$(\rho_\psi(w)\Phi)(x)=\psi\big(x\cdot\tilde e_2(w)+\tfrac12\,\tilde e_1(w)\cdot\tilde e_2(w)\big)\,\Phi(x+\tilde e_1(w)).$$ For $z\in M_{m\times n}(\mathbb A_E)$ the matrix $z\Delta^{\mathsf T}\in\mathbb W$ is $(z\,|\,z)$.

**The Weil representation.** The hypothesis concerns quadruples $(\tilde e,\omega,S,l)$ with the following four properties.

1. $\tilde e$ is a system of coordinates on $\mathbb W$ indexed by $\kappa$ that maps $M_{m\times2n}(E)$ into $F^\kappa\times F^\kappa$.
2. $\omega$ is a homomorphism from $G$ to the linear endomorphisms of the space of functions on $\mathbb A^\kappa$ with the following two properties. It is regular for $\tilde e$: the four conditions of a regular homomorphism in ([Setting for theta lifts between unitary groups of a CM extension: base data, Hermitian data, Weil representations, theta integrals](https://andrewodesky.com/rh/lean/GlobalTheory.IndefiniteRowSideFullHecke.WeilTensorModels.Base.IsGood/)) hold with $\tilde J_Y$, $\mathbb W$ and the present $\kappa$ in the places of $J_B$, $M_{n\times d}(\mathbb A_E)$ and $\{1,\ldots,n\}\times\{1,\ldots,d\}$, and with the operators $\rho_\psi$ defined by $\tilde e$. It satisfies the Siegel formula for $\chi$: if $l'$ is a tempered linear functional with $$l'\big(\rho_\psi(z\Delta^{\mathsf T})\Phi\big)=l'(\Phi)\qquad\big(z\in M_{m\times n}(\mathbb A_E),\ \Phi\in\mathcal S(\mathbb A^\kappa)\big),$$ then $$l'\big(\omega(p)\Phi\big)=\chi(\det t_p)\,\big|N_{\mathbb A_E/\mathbb A}\det t_p\big|_{\mathbb A}^{m/2}\,l'(\Phi)\qquad\big(p\in\mathcal P,\ \Phi\in\mathcal S(\mathbb A^\kappa)\big).$$
3. $S$ is a homomorphism from $U(A)(\mathbb A)$ to the linear endomorphisms of the same space that satisfies the same four conditions, with $g\in U(A)(\mathbb A)$ in the place of $h$ and with the relation $S(g)\rho_\psi(w)\Phi=\rho_\psi(gw)\,S(g)\Phi$, for $w\in\mathbb W$, as the second of them.
4. $l$ is a tempered linear functional on the space of functions on $\mathbb A^\kappa$ such that, for every $\Phi\in\mathcal S(\mathbb A^\kappa)$, $$l\big(\rho_\psi(z\Delta^{\mathsf T})\Phi\big)=l(\Phi)\quad\big(z\in M_{m\times n}(\mathbb A_E)\big),\qquad l\big(S(g)\Phi\big)=l(\Phi)\quad\big(g\in U(A)(\mathbb A)\big),$$ and the sum $$\sum_{y\in M_{m\times n}(E)}l\big(\rho_\psi((y\,|\,{-y}))\Phi\big)$$ converges to $\theta(\Phi)$.

**Hypothesis (Siegel–Weil formula for a definite space).** Let $A$, $Y$, $G$ and $\chi$ be as above, let $\kappa$ be a finite set, and let $(\tilde e,\omega,S,l)$ have the four properties. Let $b$ be a frame for $Y$, $K$ the standard compact subgroup for $b$ and $a$ a height function for $K$. Let $\mu$ be a left Haar measure on $U(A)(\mathbb A)$ and $D\subset U(A)(\mathbb A)$ a fundamental domain for left multiplication by $U(A)(F)$ with respect to $\mu$. Let $\Phi\in\mathcal S(\mathbb A^\kappa)$ be such that the functions $\omega(k)\Phi$, $k\in K$, span a finite-dimensional complex vector space. Put $$s_0=\frac{m-n}2,\qquad f_s(x)=a(x)^{s-s_0}\,l\big(\omega(x)\Phi\big)\quad(s\in\mathbb C,\ x\in G),\qquad c_{m,n}=\begin{cases}1,&n<m,\\2,&m\le n.\end{cases}$$ Then for every $x\in G$ there are a meromorphic function $\mathcal E_x$ on $\mathbb C$ and a real number $R$ such that

1. for every $s\in\mathbb C$ with $\operatorname{Re}s>R$, the Eisenstein sum of $f_s$ at $x$ converges to $\mathcal E_x(s)$;
2. $\mathcal E_x$ is holomorphic at $s_0$, and $$\mathcal E_x(s_0)=c_{m,n}\cdot\frac1{\mu(D)}\int_D\theta\big(\omega(x)\,S(g)\,\Phi\big)\,d\mu(g).$$
