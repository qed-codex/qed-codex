---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/EulerFactorBounds/DetChar.lean",
  "declarations": [
    "UpperTheory.V.Z.Kato.Nb.sDetChar"
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

## A quadratic Frobenius relation determines the determinant

[Theorem AGR.0289](https://andrewodesky.com/rh/lean/UpperTheory.V.Z.Kato.Nb.sDetChar/)

Let $\ell$ be prime, $\Omega$ an algebraic closure of $\mathbb Q$, and $G_{\mathbb Q}=\operatorname{Gal}(\Omega/\mathbb Q)$. Let $$\rho:G_{\mathbb Q}\to\operatorname{GL}_2(\overline{\mathbb Q}_\ell),\qquad\chi:G_{\mathbb Q}\to\overline{\mathbb Q}_\ell^\times$$ be continuous. Suppose some $\rho(s)$ is not a scalar matrix. Let $S$ be a finite set of rational primes. For every $p\notin S$, every valuation of $\Omega$ above $p$, and every Frobenius lift $\sigma$ in its decomposition group, suppose there is $a\in\overline{\mathbb Q}_\ell$ with $$\rho(\sigma)^2-a\rho(\sigma)+\chi(\sigma)I_2=0.$$ Then $\det\rho(s)=\chi(s)$ for every $s\in G_{\mathbb Q}$.
