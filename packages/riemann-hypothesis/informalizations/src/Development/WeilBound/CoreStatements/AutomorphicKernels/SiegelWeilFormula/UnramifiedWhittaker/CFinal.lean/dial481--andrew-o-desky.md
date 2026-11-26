---
{
  "module": "src/Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/UnramifiedWhittaker/CFinal.lean",
  "declarations": [
    "PositivityTheory.SiegelWeilFormula.Gunr.locC"
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

## An unramified local Whittaker integral

[Theorem THETA.0090](https://andrewodesky.com/rh/lean/PositivityTheory.SiegelWeilFormula.Gunr.locC/)

Let $F,E$ be number fields with an $F$-automorphism $\sigma$ of $E$, let $v$ be a finite place of $F$, and put $k=F_v$, $A=k\otimes_FE$ and $q=\#\kappa_v$. Fix an $F$-basis of $E$, its coordinate-integer lattice $S\subset A$, a ring endomorphism of $S$ inducing $\sigma$, a nonzero uniformizer candidate $\varpi\in\mathcal O_k$ with $|\varpi|<1$, and $\varepsilon\in\mathbb Z$. Assume the unramified quadratic ring conditions of ([An unramified Hermitian representation-density formula](https://andrewodesky.com/rh/lean/GlobalTheory.T.unramified_local_formula/)) for $(S,\sigma,\varpi,q,\varepsilon)$, that $A^\sigma=k$, that $|2|=1$, and that $S$ is self-dual under the trace pairing. Let $J\in\operatorname{Mat}_M(E)$ and $T\in\operatorname{Mat}_n(E)$ be integral and unimodular over $S$ for the given involution, with $T$ Hermitian. Let $\psi:k\to\mathbb C$ be a continuous additive character with annihilator of $\mathcal O_k$ equal to $\mathcal O_k$.

Use self-dual measures $dY$ on $A^{M\times n}$ and $db$ on the Hermitian matrices, and any additive Haar measure $\nu$ on $A^n$. Put $L=S^n$, $$b_0(U,V)=\tfrac12\operatorname{Tr}_{A/k}\operatorname{tr}(UV),\quad a(b)=\frac{\nu(L+bL)}{\nu(L)},$$ $$W_T(z,b)=a(b)^{-(z-(M-n)/2)}\left(\int_{S^{M\times n}}\psi(b_0(b,Y^*JY))\,dY\right)\psi(-b_0(T,b)).$$ For every $z\in\mathbb C$ with $\Re z>n^2$, $W_T(z,\cdot)$ is integrable and $$\int W_T(z,b)\,db=\prod_{i=0}^{n-1}\left(1-\varepsilon^{M+i}q^{-(2z+n-i)}\right).$$
