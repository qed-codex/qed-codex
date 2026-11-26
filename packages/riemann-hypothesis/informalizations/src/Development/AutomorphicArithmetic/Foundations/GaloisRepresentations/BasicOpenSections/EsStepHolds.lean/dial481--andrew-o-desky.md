---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/BasicOpenSections/EsStepHolds.lean",
  "declarations": [
    "UpperTheory.Gal.Mod.towES_holds"
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

## Inertia and a Frobenius polynomial on a Hecke eigenspace

[Theorem AGR.0057](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Mod.towES_holds/)

Let $\ell,p$ be rational primes and $f,n\ge0$. Let $O$ be a commutative discrete valuation domain in which $p$ is not a unit, let $K$ be an $O$-algebra that is a field with $p\ne0$, and assume every residue-field element satisfies $a^{p^f}=a$. Let $\Omega$ be an algebraically closed extension of $K$. Let $V$ be a valuation subring of $\Omega$ containing the image of $O$, whose valuation $v$ satisfies $v(a)<1$ for every $a$ in the maximal ideal of $O$, and $v(\ell)=1$.

Let $L$ be a field over $\mathbb Q_\ell$. Fix a Hecke correspondence system on a smooth projective $K$-scheme $Z$, indexed by a set $\Gamma$, with each source map finite etale. Fix $\theta:\Gamma\to L$, and let $W$ be the simultaneous eigenspace with eigenvalues $\theta$ for the pullback-trace operators on total geometric etale cohomology, after extending scalars to $L$. Assume the source's complete smooth projective integral cover package over $O$ for this system, and its correspondence congruence condition for $(p,f,n,\vartheta)$, where $\vartheta:\mathbb N\to L$. Assume $W$ is stable under every $\sigma\in\operatorname{Aut}_K(\Omega)$, and write $\rho(\sigma)$ for the induced action.

For every $\sigma$ with $\sigma(V)\subset V$ and every $x\in W$, the condition $v(\sigma a-a)<1$ for all $a\in V$ implies $\rho(\sigma)x=x$. If instead $v(\sigma a-a^{p^f})<1$ for all $a\in V$, then $$\sum_{j=0}^n(-1)^j(p^f)^{\binom j2}\vartheta(j)\rho(\sigma^{-1})^{n-j}x=0.$$
