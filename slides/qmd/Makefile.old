# Variables
PANDOC = quarto render
OUTPUT_DIR = ../pdf
THEME = metropolis

# Find all markdown files in the current directory
MD_FILES = $(wildcard *.qmd)
PDF_FILES = $(patsubst %.qmd,$(OUTPUT_DIR)/%.pdf,$(MD_FILES))

# Default target
all: $(PDF_FILES)

# Rule to generate PDF from markdown
$(OUTPUT_DIR)/%.pdf: %.qmd
	mkdir -p $(OUTPUT_DIR) $(TEMP_DIR)
	$(PANDOC) $< -t beamer -V theme:$(THEME) -o $(patsubst %.qmd,%.pdf,$<) --quiet --highlight-style=espresso
	mv $(patsubst %.qmd,%.pdf,$<) $(OUTPUT_DIR)

# Clean up generated files
clean:
	rm -f $(PDF_FILES)
