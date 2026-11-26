---
{
  "module": "src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SphericalGaloisCompatibility/PAdicSplitting/LocalGlobalCompatAtIwahoriFixedOfUnlinked.lean",
  "declarations": [
    "UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked"
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

## Inertial comparison for separated level-one support

[Theorem AGR.0159](https://andrewodesky.com/rh/lean/UpperTheory.Gal.ToralGalois.R2.localGlobalCompatAtIwahoriFixed_of_unlinked/)

Assume the universal local-comparison assertion of ([Local comparison for unlinked character support](https://andrewodesky.com/rh/lean/UpperTheory.Gal.ToralGalois.galoisCompat_unlinkedSupport_of_spherical/)). Let $E$ be a CM field, $a\ge1$, $\ell$ prime, $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$, and $\pi$ a regular algebraic polarized cuspidal representation of $\mathrm{GL}_a(\mathbb A_E)$. Let $r$ be any continuous semisimple representation weakly attached to $\pi$ as in ([Weak attachment and spherical comparison for polarized cusp forms](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.coreAll_of/)).

At a finite place $v$, write $k=E_v$ and $\sigma=\pi_v$. Assume $$\sigma^{K_1}\ne0,\qquad K_1=\ker(\mathrm{GL}_a(\mathcal O_k)\longrightarrow\mathrm{GL}_a(k_v)).$$ Suppose either that the supercuspidal support of $\sigma|\det|^{(1-a)/2}$ consists of characters with no two constituents related by $|\det|$, or that $k$ is continuously isomorphic to $\mathbb Q_p$ for a prime $p$ and the support constituents of rank at least two are pairwise inequivalent up to unramified twist. The latter condition is required in every supercuspidal support multiset and counts repeated occurrences.

For every local correspondence satisfying the conditions described in ([Local support tests for zero-monodromy parameters](https://andrewodesky.com/rh/lean/UpperTheory.Gal.Int.Row.plainTor_of_tor/)), put $y_v=\operatorname{rec}(\sigma|\det|^{(1-a)/2})$ and assume $N_{y_v}=0$.

If $v\nmid\ell$, the parameter $x_v$ of $r$ has $N_{x_v}=0$ and $$\det(T-x_v(t))=\det(T-y_v(t))\qquad(t\in I_k).$$ If $v\mid\ell$, the restriction of $r$ is de Rham and potentially semistable, its parameter has zero monodromy, and the same equality holds for every $t\in I_k$. Its jumps at each induced embedding $\tau$ are any integer multiset mapping to $\{(a-1)/2-z:z\in\operatorname{Inf}_{\iota\tau}(\pi)\}$ in $\mathbb C$.
