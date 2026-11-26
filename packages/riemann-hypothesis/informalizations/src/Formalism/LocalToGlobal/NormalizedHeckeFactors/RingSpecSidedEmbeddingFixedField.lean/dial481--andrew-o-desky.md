---
{
  "module": "src/Formalism/LocalToGlobal/NormalizedHeckeFactors/RingSpecSidedEmbeddingFixedField.lean",
  "declarations": [
    "Formalism.L2.NC.NChiData",
    "Formalism.L2.NC.NormalizedCharacterCompatibility"
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

## Normalized Hecke characters and coefficient rings

[Definition / hypothesis ARAK.D229](https://andrewodesky.com/rh/lean/Formalism.L2.NC.NChiData/)

Use ([Family fields and Galois data](https://andrewodesky.com/rh/lean/Formalism.HC.Frame/)), ([Galois representations and coefficient twists](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NData/)) and ([Integral theta expansions and local parameters](https://andrewodesky.com/rh/lean/Formalism.BasicNotions.NExp/)). A Hecke character in this hypothesis is a continuous homomorphism from the ideles of $E$ to $\mathbb C^\times$ trivial on $E^\times$; it need not be unitary. Write $K$ for the coefficient field and $K_0\subseteq K$ for the designated fixed coefficient subfield.

Hypothesis (normalized character comparisons). Choose Hecke characters $\mu_{0,j}$ for every natural $j$, an auxiliary character $\eta$, characters $\delta_i$ for twist indices, characters $\psi_a$ for local records, and $\chi_{i,\lambda}$ for abelian theta labels. Choose two embeddings $e_{i,b}:K_0\to\operatorname{Frac}(O_i)$ for each twist index. Put $$\chi^{(1)}_{i,j}=\mu_{0,j}\delta_i\eta^{-1},\qquad \lambda_{i,\lambda}=\mu_{0,j(i,\lambda)}\delta_i\chi_{i,\lambda}^{-1}.$$

Use the following precise reading convention. Given a coefficient Galois character $\rho:G_E\to A^\times$, maps $A\to L$ and $K_0\to L$, a Hecke character $\chi$ and an integer $u$, require that outside a finite set of primes $P$ there are $\alpha_P\in\mathbb C$ and $x_P\in K_0$ such that $\chi$ is unramified at $P$, its value at every local uniformizer is $\alpha_P$, and $$\jmath(x_P)=\alpha_P^{-1}(NP)^{u/2},\qquad \rho(\operatorname{Frob}_P)=x_P$$ after the indicated coefficient maps. The latter equality holds for every Frobenius element of the fixed valuation above $P$. When the comparison target is $\mathbb C$, use $K_0=\mathbb C$ and its identity embedding in this convention.

The recorded twisting character $\psi_a^{\rm Gal}$ reads $\psi_a$ with exponent zero through the recorded complex embedding of $O_a$. The recorded delta character reads $\delta_i$ with exponent zero through the prescribed true-side base embedding. Equal delta-prime sets have equal Hecke characters $\delta_i$.

At every selected stage $1\le j\le m$ and side $b$, the first recorded Galois character reads $\chi^{(1)}_{i,j}$ with exponent $-r$ through the prescribed side embedding of $K_0$ into the base fraction field. Every recorded abelian-label Galois character reads $\lambda_{i,\lambda}$ with exponent zero through $e_{i,b(i,\lambda)}$.

If $x\in K_0$ is represented by an element $y\in O_i^0$ through its prescribed side embedding, then $$e_{i,b}(x)=\text{the image of }y\text{ in }\operatorname{Frac}(O_i).$$ The character $\eta$ is unramified at every finite prime. At every chosen CM embedding its infinite local character is $z\mapsto z/|z|$: this equality is required for every continuous extension of that embedding to its infinite completion.
