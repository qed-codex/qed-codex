---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/LocalCharacterIntegrals/LocFin2.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormula.SwLocFin.locFin2",
    "PositivityTheory.SiegelWeilFormula.SwLocFin.locFinX"
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

## Entire continuation of a local oscillatory integral at a regular Gram value

[Theorem THETA.1183](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.SwLocFin.locFinX/)

Let $E/F$ be a CM extension of number fields with conjugation $\sigma$, let $J\in M_M(E)$ be nonsingular Hermitian, and let $n\ge0$. Fix a continuous, nontrivial, unit-modulus additive character $\psi:\mathbb A_F/F\to\mathbb C^\times$, a finite place $v$ of $F$, and its local component $\psi_v$. Put $k=F_v$, $E_v=k\otimes_FE$, $\mathcal X=(E_v^M)^n$, and let $\mathcal H_n$ be the Hermitian $n\times n$ matrices over $E_v$. Write $$G(X)_{ab}=\sigma(X_a)^tJX_b,\qquad \langle S,T\rangle=\tfrac12\operatorname{Tr}_{E_v/k}\operatorname{tr}(ST).$$ Choose measures $\mu$ on $\mathcal X$ and $\nu$ on $\mathcal H_n$ self-dual for $\psi_v(\sum_a\operatorname{Tr}_{E_v/k}(\sigma(X_a)^tJY_a))$ and $\psi_v(\langle S,T\rangle)$, respectively. Let $\lambda$ be additive Haar measure on $E_v^n$, and $L_1,L_2\subset E_v^n$ compact open additive subgroups. For a Schwartz–Bruhat function $\Phi$ on $\mathcal X$, suppose $g:\mathcal H_n\to\mathbb C$ is continuous on the invertible locus and satisfies $$\int_{G^{-1}(S)}\Phi\,d\mu=\int_S g\,d\nu$$ for every compact $S$ in that locus. Define $$a(b)=\frac{\lambda(L_1+bL_2)}{\lambda(L_1)},\quad s_0=\frac{M-n}{2},\quad J_\Phi(b)=\int_{\mathcal X}\Phi(X)\psi_v(\langle b,G(X)\rangle)\,d\mu(X).$$ For every invertible $T\in\mathcal H_n$, there exists an entire function $W:\mathbb C\to\mathbb C$ with $W(s_0)=g(T)$, and there is $t\in\mathbb R$ such that for $\operatorname{Re}z>t$ the integrand below is integrable and $$W(z)=\int_{\mathcal H_n}a(b)^{-(z-s_0)}J_\Phi(b)\psi_v(-\langle T,b\rangle)\,d\nu(b).$$

## An entire continuation of a local Hermitian Fourier integral

[Theorem THETA.1549](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.SwLocFin.locFin2/)

Let $E/F$ be a CM extension, $J$ a nondegenerate Hermitian form on $E^M$, and $0\le n<M$. Choose a continuous unitary nontrivial character $\psi$ of $\mathbb A_F/F$, a finite place $v$, and put $k=F_v$, $B=k\otimes_FE$, $V=(B^M)^n$, $\mathcal H=\operatorname{Herm}_n(B)$. Let $q:V\to\mathcal H$ be the Gram map. Use self-dual measures $\mu$ on $V$ for the trace-Hermitian pairing and $\nu$ on $\mathcal H$ for $$\langle S,T\rangle=\tfrac12\operatorname{Tr}_{B/k}\operatorname{tr}(ST),$$ with local character $\psi_v$. Choose an additive Haar measure $\ell$ on $B^n$ and compact open additive subgroups $L_1,L_2\subseteq B^n$, and put $$N(b)=\frac{\ell(L_1+bL_2)}{\ell(L_1)}.$$ Let $\Phi$ on $V$ be locally constant and compactly supported, and let $g:\mathcal H\to\mathbb C$ be continuous on the nonsingular locus with $$\int_{q^{-1}(S)}\Phi(X)\,d\mu(X)=\int_Sg(T)\,d\nu(T)$$ for every compact set $S$ of nonsingular Hermitian matrices. For a nonsingular $T\in\mathcal H$, define $$J_\Phi(b)=\int_V\Phi(X)\psi_v(\langle b,q(X)\rangle)\,d\mu(X),\qquad s_0=(M-n)/2.$$ There is an entire function $W_T:\mathbb C\to\mathbb C$ with $W_T(s_0)=g(T)$, and some $t\in\mathbb R$ such that for $\operatorname{Re}s>t$ the following integrand is integrable and $$W_T(s)=\int_{\mathcal H}N(b)^{-(s-s_0)}J_\Phi(b)\psi_v(-\langle T,b\rangle)\,d\nu(b).$$
