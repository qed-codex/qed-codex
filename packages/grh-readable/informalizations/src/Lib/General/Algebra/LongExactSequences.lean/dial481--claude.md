---
{
  "module": "src/Lib/General/Algebra/LongExactSequences.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "Claude",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/LongExactSequences.lean",
  "source_commit": "72fead102f663d5c7a407964a13dc0cf9d977207",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [72fead1](https://github.com/lsernau/grh-lean/blob/72fead102f663d5c7a407964a13dc0cf9d977207/grh/src/Lib/General/Algebra/LongExactSequences.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Long exact sequences, four and five lemmas, and Ext with disjoint unions and products

Long exact sequences of abelian groups are packaged as a structure, so that diagram chases, among
them the four and five lemmas, are proved once for all cohomology sequences. In the category
`New.Variety.AbFunctor C` of functors from `C` to abelian groups, with `New.Variety.H N F n`
denoting Ext^n(N, F), short exact sequences in either variable give long exact Ext sequences, and
comparison maps give morphisms between them.

## Main definitions and results

* `New.Variety.LongExactSeq`, `New.Variety.LongExactSeq.Hom`: the sequences and their morphisms.
* `New.Variety.LongExactSeq.Hom.four_lemma` (four lemma) and
  `New.Variety.LongExactSeq.Hom.five_lemma` (five lemma).
* `New.Variety.LongExactSeq.contravariant`, `New.Variety.LongExactSeq.covariant`: the long exact Ext
  sequences of a short exact sequence in the first and in the second variable;
  `New.Variety.Comparison.pull_hom_contravariant` and `New.Variety.Comparison.pull_hom_covariant`
  say that comparison maps give morphisms between them.
* `New.Variety.isCohomEquiv_iff_subsingleton`: in a short exact sequence 0 → X₁ → X₂ → X₃ → 0, the
  map X₁ → X₂ is an equivalence for F iff the quotient X₃ has no cohomology with values in F.
* `New.Variety.H.sigma_bijective`: the cohomology `New.Variety.H (freeAb.obj Y) F n` of a disjoint
  union `Y = New.Variety.sigma X` of set-valued functors is the product of the cohomology groups of
  the `X i`, by pull-back (`New.Variety.H.map`) along the inclusions.
* `New.Variety.H.pi_bijective`: the map Ext^n(N, ∏ F_i) → ∏ Ext^n(N, F_i) is bijective, for the
  objectwise product `New.Variety.piAbFunctor`.

Notions from other files:
* `New.Variety.IsCohomEquiv`: α: N' → N is an equivalence for F: the pull-back
  Ext^n(N,F) → Ext^n(N',F) is bijective for every n; `New.Variety.AllBijective f` says that every
  map f n is bijective.



## Long exact sequences, their morphisms and their rotation

* `New.Variety.LongExactSeq.rotate`: the same sequence with a `0` put in front, so that the terms
  `C (n - 1)`, `A n`, `B n` take the three places; a statement about one place then applies to the
  other two. `New.Variety.LongExactSeq.Hom.rotate` does the same for a morphism of sequences.


### `LongExactSeq.`

 A long exact sequence of abelian groups 0 → A⁰ → B⁰ → C⁰ → A¹ → B¹ → C¹ → ⋯. 

### `LongExactSeq.A, LongExactSeq.B, LongExactSeq.C`

 The first terms A n of the sequence, the middle terms B n and the third terms C n. 

### `LongExactSeq.f`

 The maps A n → B n. 

### `LongExactSeq.g`

 The maps B n → C n. 

### `LongExactSeq.δ`

 The connecting maps C n → A (n + 1). 

### `LongExactSeq.injective_f`

 Exactness at A 0: the first map A 0 → B 0 is injective. 

### `LongExactSeq.exact_f_g`

 Exactness at B n. 

### `LongExactSeq.exact_g_delta`

 Exactness at C n. 

### `LongExactSeq.exact_delta_f`

 Exactness at A (n + 1). 

### `LongExactSeq.Hom`

 Given additive maps a n, b n, c n on the terms of long exact sequences L and L', the statement
that they form a morphism L → L', that is commute with the maps f, g and the connecting maps δ. 

### `LongExactSeq.Hom.comm_f`

 The square formed by a n, b n and the maps A n → B n commutes. 

### `LongExactSeq.Hom.comm_g`

 The square formed by b n, c n and the maps B n → C n commutes. 

### `LongExactSeq.Hom.comm_delta`

 The square formed by c n, a (n + 1) and the connecting maps C n → A (n + 1) commutes. 

### `LongExactSeq.rotate`

 The sequence L moved by one place, 0 → 0 → A⁰ → B⁰ → C⁰ → ⋯: its terms in degree n are
C^(n-1), Aⁿ, Bⁿ, with C^(-1) = 0. 

### `LongExactSeq.rotateMap`

 Maps cₙ : Cⁿ → C'ⁿ between the third terms of L and L' give maps between the first terms of the
rotated sequences: the zero map in degree 0 and cₙ in degree n + 1. 

### `LongExactSeq.Hom.rotate`

 A morphism (a, b, c) of long exact sequences L → L' gives one between the rotated sequences,
whose components are `rotateMap c` = (0, c₀, c₁, …), a and b. 


## Four and five lemmas and the long exact Ext sequences


 ### Bijectivity up to a given place and bijective sides of a square 

### `BijectiveUpTo`

 For maps f_n: A_n → B_n, the first r of the conditions: f₀ injective, f₀ surjective, f₁
injective, f₁ surjective, and so on. 

### `BijectiveUpTo.congr`

 If bijections a_n: A_n → A'_n and b_n: B_n → B'_n carry the maps f_n to the maps g_n, then f
satisfies the first r conditions of `BijectiveUpTo` (f₀ injective, f₀ surjective, f₁ injective, …)
exactly when g does. 

### `Comparison.bijective_iff_of_comm_sq`

 In a commutative square with two opposite sides bijective, one of the other two sides is
bijective iff the other is. 

 ### The long exact Ext sequences and the diagram chases 

### `contravariant`

 For 0 → S₁ → S₂ → S₃ → 0 short exact, the long exact sequence Ext^n(S₃,F) → Ext^n(S₂,F) →
Ext^n(S₁,F) → Ext^{n+1}(S₃,F) of abelian groups. 

### `covariant`

 For 0 → S₁ → S₂ → S₃ → 0 short exact, the long exact sequence Ext^n(N,S₁) → Ext^n(N,S₂) →
Ext^n(N,S₃) → Ext^{n+1}(N,S₁) of abelian groups. 

### `bijective_succ_family`

 Let (a i, b i, c i) be morphisms from the long exact sequence L to the sequences L' i. If the
connecting maps δ out of degree n are onto in L and in all L' i, and the maps x ↦ (b i n x)ᵢ and
x ↦ (c i n x)ᵢ into the products are bijective, then so is x ↦ (a i (n + 1) x)ᵢ. 

### `eq_zero_of_delta_eq_zero`

 The injectivity chase for a morphism (a, b, c) from a long exact sequence L to a second one L':
if a is onto and b is injective in degree n, then an element of the third term Cⁿ of L that is
killed by c and by the connecting map δ is zero. 

### `exists_preimage_mod_f`

 For a morphism (a, b, c) from a long exact sequence L to a second one L', with maps f' : A' → B'
and g' : B' → C': if a is injective in degree n + 1 and `c x = g' y`, then `x = g z` for some z
such that `y - b z` lies in the image of f'. 

### `exists_preimage`

 The surjectivity chase for a morphism h = (a, b, c) of long exact sequences L → L': if a is onto
in degree n and injective in degree n + 1, and `c x = g' y`, then some z has `b z = y` and
`g z = x`. 

### `rotateMap_injective`

 For maps c m : C m → C' m, the component in degree n of `rotateMap c` (c m for n = m + 1, a map
between zero groups for n = 0) is injective if c m is so for n = m + 1. 

### `rotateMap_surjective`

 For maps c m : C m → C' m, the component in degree n of `rotateMap c` (c m for n = m + 1, a map
between zero groups for n = 0) is surjective if c m is so for n = m + 1. 

### `four_lemma`

 Four lemma for a morphism h = (a, b, c) from L to L', long exact sequences
0 → A⁰ → B⁰ → C⁰ → A¹ → ⋯: if b satisfies the first r of the conditions "injective in degree 0,
surjective in degree 0, injective in degree 1, …" (`BijectiveUpTo`) and c the first r − 1, then a
satisfies the first r. 

### `five_lemma`

 Five lemma for the morphism h = (a, b, c) from the long exact sequence L to L': if c is
bijective in all degrees (`AllBijective`), then b is bijective in all degrees exactly when a is. 

### `LongExactSeq.f_injective_of_g_surjective`

 In a long exact sequence, if all maps g : B m → C m with m < n are surjective, then
f : A n → B n is injective. 

### `Comparison.pull_apply`

 The comparison map of c = (φ, β), with φ = c.functor : C' ⥤ C and β = c.coeffHom : φ ⋙ F → F',
along α: N' → N∘φ sends a class x to α · (x∘φ) · β, where · is the composition of Ext classes and
x∘φ is the restriction of x along φ. 

### `Comparison.pull_hom_contravariant`

 Let c = (φ, β) be a comparison from F on C to F' on C', that is φ : C' ⥤ C and β : φ ⋙ F → F',
and let τ be a morphism from S' to the restriction of S along φ, for short exact complexes S and
S'. Then the maps c.pull τᵢ (restrict along φ, push by β, pull back by τᵢ) form a morphism from
the contravariant Ext sequence of (S, F) to that of (S', F'). 

### `Comparison.pull_hom_covariant`

 For short exact complexes S and S', a morphism τ from the restriction of S along φ to S' and a
map α : N' → N ∘ φ give a morphism from the covariant Ext sequence of (N, S) to that of (N', S').
Its components are the maps pull ⟨φ, τᵢ⟩ α: restrict along φ, push by τᵢ and pull back by α. 

### `isCohomEquiv_iff_subsingleton`

 For 0 → X₁ → X₂ → X₃ → 0 short exact, X₁ → X₂ induces bijections on Extⁿ(-, F) for all n (it is
a cohomological equivalence for F) exactly when Extⁿ(X₃, F) = 0 for all n. 

### `isCohomEquiv_quotient_of_acyclic`

 For a short exact sequence 0 → X₁ → X₂ → X₃ → 0 of functors with Extⁿ(X₁,F) = 0 for all n,
the pull-back Extⁿ(X₃,F) → Extⁿ(X₂,F) is bijective for all n. 

 ## Cohomology of disjoint unions 

### `New.Variety.H.sigma_bijective`

 Let Y = `New.Variety.sigma X` be the disjoint union of a family of set-valued functors X_i.
Write ℤ[Y] = `freeAb.obj Y` for the free abelian functor on Y and H^n(Y, F) for Ext^n(ℤ[Y], F).
Then H^n(Y, F) is in bijection with the product of the H^n(X_i, F): the bijection sends a class to
the family of its pull-backs (`H.map`) along the maps ℤ[X_i] → ℤ[Y] induced by the inclusions. 


## Acyclic covers and Ext of products of coefficients

* `New.Variety.exists_acyclic_cover`: each `M` is a quotient of the free abelian functor on a
  disjoint union of representable functors, with surjective connecting maps in `Ext`; this allows
  dimension shifting.


### `kerComplex`

 For a morphism β: M → G of abelian-group-valued functors, the three-term complex ker β → M →
G, with the kernel taken objectwise and included into M. 

### `exists_acyclic_cover`

 Every functor M from C to abelian groups is a quotient, by some map g, of the free abelian
functor ℤ[⊔ h_{c_i}] on a disjoint union of representable functors h_{c_i} = `reprBy (c i)`, such
that, for K = ker g (the first term of the short exact sequence `kerComplex g`), the connecting map
Ext^n(K,F) → Ext^{n+1}(M,F) of the Ext sequence `contravariant` is surjective for all F and n. 

### `piAbFunctor.lift`

 Given natural transformations N→F_i for each index i, the natural transformation from N to
the pointwise product of the functors F_i having these as components. 

### `H.pi_bijective`

 Ext commutes with products in the coefficients: the map Ext^n(N, ∏ F_i) → ∏ Ext^n(N, F_i)
sending a class to the family of its push-forwards (`push`) along the projections π F i of the
objectwise product `piAbFunctor F` is bijective. 
