---
{
  "module": "src/Development/AutomorphicArithmetic/AutomorphicVarieties/GeneratorCountTuples/LemmaK.lean",
  "declarations": [
    "UpperTheory.V.HasMuQ",
    "UpperTheory.V.LemmaK",
    "UpperTheory.V.kBound"
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

## A uniform bound for second cyclotomic cohomology

[Definition / hypothesis GC.D081](https://andrewodesky.com/rh/lean/UpperTheory.V.LemmaK/)

For a real number $C_K$, consider the following condition. Let $\ell$ be any prime and $L$ any totally complex number field containing a primitive $\ell$th root of unity when $\ell\ne2$, and a primitive fourth root of unity when $\ell=2$. Fix an algebraic closure $\Omega/L$. Let $S_\ell$ be the finite primes of $L$ dividing $\ell$, and let $G_{L,S_\ell}$ be the Galois group of the maximal subextension of $\Omega/L$ unramified at every finite prime outside $S_\ell$, with its profinite topology. Write $\varepsilon_\ell:G_{L,S_\ell}\to\mathbb Z_\ell^\times$ for the character whose pullback to $\operatorname{Gal}(\Omega/L)$ is the $\ell$-adic cyclotomic character.

For every integer $e\ge1$, let $\mathbb Z_\ell(e+1)$ be the additive group $\mathbb Z_\ell$, with its $\ell$-adic topology and action $g\cdot z=\varepsilon_\ell(g)^{e+1}z$. Then the continuous cohomology group $H^2(G_{L,S_\ell},\mathbb Z_\ell(e+1))$ is finite and, writing $n=[L:\mathbb Q]$ and $D=|\operatorname{disc}(L)|$, satisfies $$\log\#H^2\bigl(G_{L,S_\ell},\mathbb Z_\ell(e+1)\bigr)\le \exp\!\left((2en)^{C_K}\log(2D)\right).$$ The condition is required for every algebraic closure and every choice of prolongations to it of the primes in $S_\ell$.

We say that a uniform bound holds if this condition holds for some real number $C_K$.
