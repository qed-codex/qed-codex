---
{
  "module": "src/Formalism/LocalToGlobal/ProjectiveLattices/IntegrableOnIntegrand.lean",
  "declarations": [
    "Formalism.L2.Pj.FJ.CuNeF",
    "Formalism.L2.Pj.FJ.ExpoMatch",
    "Formalism.L2.Pj.FJ.LatZ"
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

## Isotropic lattices and Fourier exponents

[Definition / hypothesis ARAK.D197](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.FJ.LatZ/)

Hypothesis (isotropic lattices and Fourier exponents). Use the original domain data at the distinguished embedding $K_0\subset\mathbb C$ in ([Original moduli uniformizations and cusp norms](https://andrewodesky.com/rh/lean/Formalism.L2.Pj.LawsM/)). Fix any selected stage $1\le j\le m$ and set $\rho=m-j$. For each domain label $c$, let $G_c$, $\Lambda_c$, $\Gamma_c$, $\Psi_c$ and $\kappa_c$ be its Gram matrix, integral lattice, arithmetic group, CM type and alternating multiplier, as defined in ([Complex uniformizations and period lattices](https://andrewodesky.com/rh/lean/ReciprocityTheory.ChartRestriction.G.FD.Data/)). Write $$h_c(v,w)=\sum_{a,b}v_a(G_c)_{ab}\bar w_b.$$ There exists in every domain an ordered family $e_1,\ldots,e_\rho\in E^r$ that is linearly independent over $E$ and satisfies $h_c(e_a,e_b)=0$ for all $a,b$. When $\rho=0$ this is the empty family.

The following conditions hold for every such family in every domain. Put $$I_e=\Lambda_c\cap\operatorname{span}_E\{e_a\},\qquad C_e=\{v\in E^\rho:\sum_a v_ae_a\in I_e\}.$$ For a submodule $C\subset E^\rho$ put $$C^{\vee_{\mathbb Z}}=\{l:\operatorname{Tr}_{E/\mathbb Q}\sum_a l_ax_a\in\mathbb Z\text{ for every }x\in C\},\qquad C^{\vee_{\mathcal O}}=\{l:\sum_a l_ax_a\in\mathcal O_E\text{ for every }x\in C\},$$ and define $X_e=\operatorname{span}_{\mathcal O_E}C_e^{\vee_{\mathbb Z}}$.

For $\beta\in M_\rho(E)$ define $$(Z_e(\beta))_{kl}=\delta_{kl}+\sum_{a,b}\beta_{ab}(e_a)_k\sum_s(G_c)_{ls}\overline{(e_b)_s},$$ $$\mathcal Z_e=\{\beta:\bar\beta^{\,T}=-\beta,\ Z_e(\beta)\in\Gamma_c\}.$$ The additive group $\mathcal Z_e$ has a $\mathbb Z$-basis of exactly $|\Psi_c|\rho^2$ matrices: these matrices are linearly independent over $\mathbb Z$, and their integral span is exactly $\mathcal Z_e$.

For every Hermitian $\chi\in M_\rho(E)$, require the equivalence $$\forall\beta\in\mathcal Z_e:\quad\sum_{\tau\in\Psi_c}\Re\tau\left(\frac{\operatorname{tr}(\chi^T\beta)}{\kappa_c/2}\right)\in\mathbb Z$$ $$\Longleftrightarrow\quad \forall l,m\in X_e^{\vee_{\mathcal O}}:\quad g_0g_1\sum_{a,b}l_a\chi_{ab}\bar m_b\in\mathcal O_E.$$ Both universal conditions and the displayed basis condition apply to all isotropic families, while existence of at least one such family is required in every domain.
