CREATE TABLE modules (
  id INTEGER PRIMARY KEY, path TEXT NOT NULL, project INTEGER NOT NULL,
  import_rank INTEGER, cut INTEGER, mask INTEGER, trace_reached INTEGER,
  removed_upstream INTEGER, upstream_rank INTEGER, spine_rank INTEGER, package TEXT NOT NULL, UNIQUE(package,path)
);
CREATE TABLE imports (
  caller INTEGER NOT NULL REFERENCES modules, dependency INTEGER NOT NULL REFERENCES modules,
  PRIMARY KEY(caller,dependency)
) WITHOUT ROWID;
CREATE TABLE declarations (
  id INTEGER PRIMARY KEY, module INTEGER NOT NULL REFERENCES modules, name TEXT NOT NULL,
  start INTEGER, end INTEGER, kind TEXT NOT NULL, kernel_mask INTEGER NOT NULL, package TEXT NOT NULL
);
CREATE TABLE trace (
  id INTEGER PRIMARY KEY, module INTEGER NOT NULL REFERENCES modules, line INTEGER NOT NULL,
  declaration INTEGER REFERENCES declarations, source_name TEXT, parent INTEGER REFERENCES trace,
  use_line INTEGER NOT NULL
);
CREATE TABLE informalizations (
  id INTEGER PRIMARY KEY, module INTEGER NOT NULL REFERENCES modules, author TEXT NOT NULL,
  writer TEXT NOT NULL, kind TEXT CHECK (kind IN ('human','ai','ai-reviewed-by-human')),
  origin TEXT NOT NULL CHECK (origin IN ('wrote','generated','other-author')), submitted_order INTEGER NOT NULL,
  license TEXT NOT NULL CHECK (license IN ('CC-BY-4.0','with-permission','Apache-2.0','MIT','CC0-1.0')), source_commit TEXT NOT NULL,
  declarations_json TEXT NOT NULL, source_url TEXT, body TEXT NOT NULL, informalization_html TEXT NOT NULL,
  agrees_with_json TEXT NOT NULL DEFAULT '{}',
  copyright TEXT, license_source TEXT, notice TEXT, changes TEXT,
  entry_type TEXT NOT NULL DEFAULT 'informalization' CHECK (entry_type IN ('informalization','source-documentation')),
  CHECK (entry_type!='source-documentation' OR origin='other-author'),
  CHECK (license NOT IN ('MIT','Apache-2.0') OR length(trim(coalesce(copyright,'')))>0
    OR (entry_type='source-documentation' AND copyright IS '')),
  CHECK (origin='other-author' OR license='CC-BY-4.0'),
  CHECK (origin!='other-author' OR source_url IS NOT NULL),
  CHECK (origin='other-author' OR (origin='wrote' AND kind IS 'human') OR
         (origin='generated' AND kind IS NOT NULL AND kind IN ('ai','ai-reviewed-by-human'))),
  UNIQUE(module,author,writer)
);
CREATE TABLE links (module INTEGER NOT NULL REFERENCES modules, author TEXT NOT NULL, url TEXT NOT NULL, label TEXT NOT NULL,
                    declaration TEXT NOT NULL, PRIMARY KEY(module,url,declaration)) WITHOUT ROWID;
CREATE INDEX links_by_declaration ON links(declaration,url);
CREATE TABLE disputes (id INTEGER PRIMARY KEY, module INTEGER NOT NULL REFERENCES modules, url TEXT NOT NULL);
CREATE TABLE summary (metric TEXT PRIMARY KEY, value INTEGER NOT NULL) WITHOUT ROWID;
CREATE VIRTUAL TABLE names USING fts5(module_path, declaration_name, content='',prefix='3 4 6',detail=none,columnsize=0);
CREATE TABLE shortnames (
  short TEXT NOT NULL, full TEXT NOT NULL, kind TEXT NOT NULL, ref INTEGER NOT NULL,
  package TEXT NOT NULL, PRIMARY KEY(short,full,kind,package)
) WITHOUT ROWID;
CREATE TABLE most_wanted (rank INTEGER PRIMARY KEY, module INTEGER NOT NULL UNIQUE REFERENCES modules);
CREATE TABLE search_counts (
  word TEXT NOT NULL, prefix TEXT NOT NULL, total INTEGER NOT NULL,
  PRIMARY KEY(word,prefix)
) WITHOUT ROWID;
CREATE TABLE proofs (id TEXT PRIMARY KEY, source TEXT NOT NULL, root_decl TEXT,
 root_module INTEGER REFERENCES modules, statement_module INTEGER REFERENCES modules, solution_module INTEGER REFERENCES modules,title TEXT NOT NULL);
CREATE TABLE proof_roles (module INTEGER REFERENCES modules, proof TEXT REFERENCES proofs, role TEXT NOT NULL CHECK(role IN ('statement','solution')), PRIMARY KEY(module,proof,role)) WITHOUT ROWID;
CREATE TABLE proof_modules (proof TEXT REFERENCES proofs, module INTEGER REFERENCES modules, PRIMARY KEY(proof,module)) WITHOUT ROWID;
CREATE INDEX proof_by_module ON proof_modules(module,proof);
CREATE INDEX proof_statement ON proofs(statement_module);
CREATE INDEX proof_solution ON proofs(solution_module);
CREATE TABLE wanted_source (package TEXT, rank INTEGER, module INTEGER REFERENCES modules, PRIMARY KEY(package,rank)) WITHOUT ROWID;

CREATE TABLE note_headings (id INTEGER PRIMARY KEY, module INTEGER NOT NULL REFERENCES modules,
 name TEXT NOT NULL, lookup TEXT NOT NULL, anchor TEXT NOT NULL, UNIQUE(module,anchor));
CREATE INDEX note_heading_lookup ON note_headings(lookup);
CREATE TABLE proof_names (lookup TEXT NOT NULL, proof TEXT NOT NULL REFERENCES proofs, name TEXT NOT NULL,
 PRIMARY KEY(lookup,proof)) WITHOUT ROWID;
