---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsAbelianSchemeQuotientByFiniteTranslationsStatement.lean",
  "declarations": [
    "GlobalTheory.T.exists_abelianScheme_quotient_by_finite_translations"
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

## An abelian-scheme quotient by finitely many translations

[Theorem AV.0314](https://andrewodesky.com/rh/lean/GlobalTheory.T.exists_abelianScheme_quotient_by_finite_translations/)

Let $S$ be a scheme, $A/S$ an abelian scheme with commutative group law, $L$ a relatively ample line bundle on $A$, and $H\le A(S)$ a finite subgroup. Suppose that for every algebraically closed field $\kappa$, every $x:\operatorname{Spec}\kappa\to S$, and $h\in H$, $$h_x=0\quad\Longrightarrow\quad h=0.$$ There are a commutative abelian scheme $A'/S$ and a group homomorphism $\pi:A\to A'$ which is finite, étale and surjective. Moreover, $\pi\circ t_h=\pi$ for $h\in H$, where $t_h$ is translation by $h$, and whenever $y,y'\in A(\kappa)$ have $\pi(y)=\pi(y')$, there is a unique $h\in H$ with $y'=t_h(y)$.
