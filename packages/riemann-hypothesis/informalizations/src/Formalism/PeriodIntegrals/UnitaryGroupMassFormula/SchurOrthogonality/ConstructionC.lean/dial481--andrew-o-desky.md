---
{
  "module": "src/Formalism/PeriodIntegrals/UnitaryGroupMassFormula/SchurOrthogonality/ConstructionC.lean",
  "declarations": [
    "PI.WSF.schurOrth_of"
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

## The normalized Fock norm as a unitary-group integral

[Theorem REP.0984](https://andrewodesky.com/rh/lean/PI.WSF.schurOrth_of/)

For each integer $N\ge0$ and weakly decreasing integer tuple $\lambda=(\lambda_1,\ldots,\lambda_N)$, put $d=\lambda_N$ when $N>0$ and $d=0$ when $N=0$, and set $\nu_i=\lambda_i-d\in\mathbb N$. Use ([Polynomial Weyl modules and row substitutions](https://andrewodesky.com/rh/lean/Formalism.GradedWeylDivisibility.dualWeyl/)) in a square $N\times N$ variable matrix $X$, and write $$\nabla_\lambda=\nabla_\nu(\mathbb C),\qquad \Delta_\lambda=\Delta_\nu(\mathbb C),\qquad v_\lambda=v_\nu.$$ Use $[\ ,\ ]_{\rm fac}$ from ([Bilinear factorial pairing of polynomials](https://andrewodesky.com/rh/lean/Formalism.L2.G.Model.TS.fockR/)) over $\mathbb C$. For polynomials $P,Q\in\mathbb C[X_{ai}]$, let $\overline Q$ denote the polynomial obtained by conjugating every coefficient of $Q$, and define $$\langle P,Q\rangle_\lambda= \frac{[P,\overline Q]_{\rm fac}}{[v_\lambda,\overline{v_\lambda}]_{\rm fac}}.$$ For $g\in\operatorname{GL}_N(\mathbb C)$ and a polynomial $f$, define $$(\rho_\lambda(g)f)(X)=\det(g)^d f(g^{\mathsf T}X).$$

Assume that the following facts hold for every $N$ and $\lambda$:

1. $\nabla_\lambda=\Delta_\lambda$.
2. Every complex subspace $V\subseteq\nabla_\lambda$ stable under $\rho_\lambda(g)$ for every $g\in\operatorname{GL}_N(\mathbb C)$ is either $0$ or $\nabla_\lambda$.
3. If $f\in\nabla_\lambda$ is fixed by $\rho_\lambda(u)$ for every upper unipotent matrix $u\in\operatorname{GL}_N(\mathbb C)$, then $f=c\,v_\lambda$ for some $c\in\mathbb C$.
4. $f(I_N)=\langle f,v_\lambda\rangle_\lambda$ for every $f\in\nabla_\lambda$.

For any such $N,\lambda$, let $\mu$ be a Borel probability measure on $M_N(\mathbb C)$ with $X\in U(N)$ for $\mu$-almost every $X$. Suppose that for every $u\in U(N)$ and every continuous $h:M_N(\mathbb C)\to\mathbb C$, $$\int h(Xu)\,d\mu(X)=\int h(X)\,d\mu(X)=\int h(uX)\,d\mu(X).$$ Then for every $f\in\nabla_\lambda$, $$\operatorname{Re}\langle f,f\rangle_\lambda=\dim_{\mathbb C}(\Delta_\lambda)\int_{M_N(\mathbb C)}|f(X)|^2\,d\mu(X).$$
