---
{
  "module": "src/Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean",
  "declarations": [
    "GlobalTheory.HeckeGal.Gab",
    "GlobalTheory.HeckeGal.IsGlobalArtin",
    "GlobalTheory.HeckeGal.exists_unique_hchar_of_finite_order",
    "GlobalTheory.HeckeGal.infConn",
    "GlobalTheory.HeckeGal.toAb",
    "GlobalTheory.Published.GlobalArtinReciprocity"
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

## The Hecke character of a finite-order Galois character

[Theorem ANT.1212](https://andrewodesky.com/rh/lean/GlobalTheory.HeckeGal.exists_unique_hchar_of_finite_order/)

Let $E$ be a number field, $\Omega/E$ a field extension, $\ell$ a prime, and $\iota:\overline{\mathbb Q}_\ell\simeq\mathbb C$ a field isomorphism. Put $G=\operatorname{Aut}_E(\Omega)$ with its Krull topology. Suppose $\operatorname{Art}:\mathbb A_E^\times\to G^{\mathrm{ab}}$, where $G^{\mathrm{ab}}$ is the topological abelianization, satisfies the global Artin-map conditions specified in the conventions. Let $r:G\to\overline{\mathbb Q}_\ell^\times$ be continuous, and suppose $m>0$ and $r^m=1$.

There is a unique Hecke character $\chi$ with $\chi^m=1$ and $$r(\sigma)=\iota^{-1}(\chi(x))\quad\text{whenever }\operatorname{Art}(x)=\sigma^{\mathrm{ab}}.$$

## Global Artin map of a number field

[Definition / hypothesis GC.D277](https://andrewodesky.com/rh/lean/GlobalTheory.HeckeGal.IsGlobalArtin/)

A global Artin map is a homomorphism from the idele group of a number field to the abelianized absolute Galois group that has the five properties of the reciprocity map of global class field theory listed below. The page also states the hypothesis that such a map exists for every number field.

**Notation.** Let $E$ be a number field and $\Omega$ an algebraic closure of $E$. Put $G_E=\operatorname{Gal}(\Omega/E)$ with the Krull topology, and let $G_E^{\rm ab}$ be the quotient of $G_E$ by the closure of its commutator subgroup, with the quotient topology. Let $\mathbb A_E=(E\otimes_{\mathbb Q}\mathbb R)\times\mathbb A_E^{\rm f}$ be the adele ring of $E$ and $\mathbb A_E^\times$ its group of units, the idele group, with the topology of the group of units of a topological ring: the topology induced by the embedding $x\mapsto(x,x^{-1})$ into $\mathbb A_E\times\mathbb A_E$. The group $E^\times$ is embedded diagonally in $\mathbb A_E^\times$. Let $(E\otimes_{\mathbb Q}\mathbb R)^{\times,0}$ be the connected component of the identity of $(E\otimes_{\mathbb Q}\mathbb R)^\times$, embedded in $\mathbb A_E^\times$ with all finite components equal to $1$.

For a finite place $v$ of $E$, let $E_v$ be the completion of $E$ at $v$ and $\mathrm Nv$ the number of elements of the residue field of $v$. The group $E_v^\times$ is embedded in $\mathbb A_E^\times$ with all other components equal to $1$. A *unit at $v$* is an element of $E_v^\times$ of valuation $0$, and a *uniformizer at $v$* is an element of $E_v^\times$ of valuation $1$, for the valuation of $E_v$ with value group $\mathbb Z$.

A valuation ring $A$ of $\Omega$ *lies over* $v$ if its maximal ideal $\mathfrak m_A$ meets the ring of integers $\mathcal O_E$ in the prime ideal of $v$. For such $A$, the *decomposition group* is $D_A=\{\sigma\in G_E:\sigma(A)=A\}$, the *inertia group* $I_A$ consists of the $\sigma\in D_A$ with $\sigma(x)-x\in\mathfrak m_A$ for all $x\in A$, and an *arithmetic Frobenius element at $A$* is an element $\sigma\in D_A$ with $\sigma(x)-x^{\mathrm Nv}\in\mathfrak m_A$ for all $x\in A$.

**Definition (global Artin map).** A *global Artin map* for $(E,\Omega)$ is a group homomorphism $$\operatorname{art}:\mathbb A_E^\times\longrightarrow G_E^{\rm ab}$$ with the following five properties.

1. $\operatorname{art}$ is surjective, continuous and open.
2. The kernel of $\operatorname{art}$ is the closure of the subgroup $E^\times\cdot(E\otimes_{\mathbb Q}\mathbb R)^{\times,0}$ of $\mathbb A_E^\times$.
3. For every finite place $v$ of $E$ and every valuation ring $A$ of $\Omega$ lying over $v$, the image under $\operatorname{art}$ of the set of units at $v$ is the image of $I_A$ in $G_E^{\rm ab}$.
4. For every such $v$ and $A$, the image under $\operatorname{art}$ of the set of uniformizers at $v$ is the set of the images in $G_E^{\rm ab}$ of the elements $\sigma^{-1}$, where $\sigma$ runs over the arithmetic Frobenius elements at $A$.
5. For every such $v$ and $A$, the closure of $\operatorname{art}(E_v^\times)$ in $G_E^{\rm ab}$ is the image of $D_A$.

**Hypothesis (existence of global Artin maps).** For every number field $E$ and every algebraic closure $\Omega$ of $E$ there is a global Artin map for $(E,\Omega)$.
