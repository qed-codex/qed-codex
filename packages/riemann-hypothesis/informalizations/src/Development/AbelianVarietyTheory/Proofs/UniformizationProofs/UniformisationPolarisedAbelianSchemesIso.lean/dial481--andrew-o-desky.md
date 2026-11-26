---
{
  "module": "src/Development/AbelianVarietyTheory/Proofs/UniformizationProofs/UniformisationPolarisedAbelianSchemesIso.lean",
  "declarations": [
    "GlobalTheory.unifPre_polarised_iso"
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

## Comparison of polarized abelian parts of uniformizations

[Theorem AV.1225](https://andrewodesky.com/rh/lean/GlobalTheory.unifPre_polarised_iso/)

Assume the three universal statements in the conventions below on global functions, base change for sections of polarization powers, and generation and very ampleness of such powers. Let $R$ be a noetherian integrally closed local domain, $I\subset R$ an ideal, and suppose $R$ is $I$-adically complete. Let $D,D'$ be degeneration data over $(R,I)$, let $A,A'$ be polarized abelian varieties over $\operatorname{Frac}R$, and let $G$ be a commutative semiabelian scheme over $R$. Suppose preliminary uniformizations $U,U'$ identify the generic fibre of $G$ with $A,A'$ and realize $D,D'$ at every infinitesimal thickening.

Write $L_G,L'_G$ for their line bundles on $G$. Suppose there is a generating line-bundle isomorphism $w_G:L'_G\simeq L_G$ respecting their rigidifications at the identity. Write $(B,L),(B',L')$ for the polarized abelian parts of $D,D'$, and $f_e:G_e\to B$, $f'_e:G_e\to B'$ for the maps from $G_e=G\times_R R/I^{e+1}$. Let $w_e:L_G|_{G_e}\simeq f_e^*L$ and $w'_e:L'_G|_{G_e}\simeq(f'_e)^*L'$ be the supplied isomorphisms.

There exist an isomorphism $\Phi:B'\simeq B$ and a generating line-bundle isomorphism $w:L'\simeq\Phi^*L$ such that, for every $e\ge0$, $$\Phi\circ f'_e=f_e,\qquad (f'_e)^*w\circ w'_e=w_e\circ(w_G|_{G_e}).$$ The second identity holds on every test-scheme point in every compatible choice of line-bundle charts.
