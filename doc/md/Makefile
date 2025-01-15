# Makefile to convert all Markdown files (*.md) to PDF using Pandoc

# Define the output directory
OUTDIR = ./pdf

# Find all Markdown files in the current directory
SRC = $(wildcard *.md)

# Define the output files in the OUTDIR with .pdf extension
PDFS = $(patsubst %.md, $(OUTDIR)/%.pdf, $(SRC))

# Pandoc options (modify the theme and additional settings as needed)
PANDOC_OPTS = --pdf-engine=xelatex --variable geometry:margin=1in --highlight-style=pygments

# Default target
all: $(PDFS)

# Rule to create the output directory
$(OUTDIR):
	mkdir -p $(OUTDIR)

# Rule to convert Markdown to PDF
$(OUTDIR)/%.pdf: %.md | $(OUTDIR)
	pandoc $(PANDOC_OPTS) $< -o $@

# Clean generated files
clean:
	rm -rf $(OUTDIR)
