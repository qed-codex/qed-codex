---
{
  "module": "Mathlib/NumberTheory/LSeries/DirichletContinuation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Andrew O'Desky",
  "origin": "other-author",
  "source": "https://andrewodesky.com/rh/",
  "source_commit": "0df444a360eaa60ab8c11dca51a86af692955474",
  "license": "with-permission"
}
---

As published on 26 November 2026.

## Induced characters and finite Euler products

[Theorem ANT.1736](https://andrewodesky.com/rh/s/z1-induced-euler-products.html)

Let $N\ge1$ be an integer and let $\chi$ be a complex Dirichlet character modulo $N$. Its conductor $f$ is the least positive divisor of $N$ from which $\chi$ is induced. Then $f\ge1$, $f\mid N$, and there is a primitive character $\chi^*$ modulo $f$ inducing $\chi$. Here induction means that $\chi(n)=\chi^*(n)$ for integers $n$ coprime to $N$, and $\chi(n)=0$ for the remaining integers; primitive means that the modulus equals the conductor.

The principal character modulo a positive integer equals $1$ on integers coprime to that modulus and $0$ otherwise. Induction preserves principal characters. A principal character of positive modulus is primitive exactly when its modulus is $1$.

More generally, let $M,N\ge1$ satisfy $M\mid N$, let $\psi$ be a complex Dirichlet character modulo $M$, and let $\psi_N$ be its induced character modulo $N$. Write $\psi_0$ for the principal character modulo $M$. For $s\in\mathbb C$ such that $\psi\ne\psi_0$ or $s\ne1$, $$L(s,\psi_N)=L(s,\psi)\prod_{p\mid N}\left(1-\psi(p)p^{-s}\right).$$ The product is over the distinct prime divisors $p$ of $N$, $p^{-s}=\exp(-s\log p)$, and $L(s,\psi)$ and $L(s,\psi_N)$ denote the meromorphic continuations of their Dirichlet series from $\Re s>1$.

## Zeta values and functional equation

[Theorem ANT.1739](https://andrewodesky.com/rh/s/z1-zeta-functional-equation.html)

Let $\zeta(s)$ denote the meromorphic continuation of $\sum_{n\ge1}n^{-s}$ from $\Re s>1$. If $\chi$ is the unique Dirichlet character modulo $1$, then its Dirichlet $L$-function satisfies $$L(s,\chi)=\zeta(s),\qquad \zeta(0)=-\frac12.$$ Let $\Gamma$ denote Euler's gamma function. For every $w\in\mathbb C$ such that $w\notin\{0,-1,-2,\ldots\}$ and $w\ne1$, $$\zeta(1-w)=2\,(2\pi)^{-w}\,\Gamma(w)\,\cos\!\left(\frac{\pi w}{2}\right)\,\zeta(w),$$ where $(2\pi)^{-w}=\exp(-w\log(2\pi))$.
