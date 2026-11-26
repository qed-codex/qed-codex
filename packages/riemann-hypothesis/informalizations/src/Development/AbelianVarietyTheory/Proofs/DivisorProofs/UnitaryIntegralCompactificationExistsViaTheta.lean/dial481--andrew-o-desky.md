---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/UnitaryIntegralCompactificationExistsViaTheta.lean",
  "declarations": [
    "GlobalTheory.UMinTop.integral_normal_model_dense"
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

## A finite normal model containing the generic scheme densely

[Theorem AG.0481](https://andrewodesky.com/rh/lean/GlobalTheory.UMinTop.integral_normal_model_dense/)

Let $o$ be a Dedekind domain finitely generated over $\mathbb Z$, and let $F$ be a characteristic-zero field. Let $b:o\hookrightarrow F$ identify $F$ with the fraction field of $o$: every $x\in F$ has $xb(d)=b(a)$ for some $a,d\in o$ with $b(d)\ne0$. Let $s:X\to\operatorname{Spec}F$ be a normal, separated, finite-type scheme, and let $f:X\to\mathbb P_o^n$ be an $o$-morphism. Suppose that for every algebraically closed field $K$ and $x\in X(K)$, there are only finitely many $y\in X(K)$ with $s(y)=s(x)$ and $f(y)=f(x)$.

There are a normal scheme $Z$, a finite morphism $p:Z\to\mathbb P_o^n$, and a dense open immersion $i_F:X\hookrightarrow Z_F$ such that $p_Fi_F=f_F$ and the composite $X\to Z_F\to Z$ also has dense image.
