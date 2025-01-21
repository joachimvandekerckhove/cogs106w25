# Variables
PANDOC = quarto render
OUTPUT_DIR = ../pdf
TEMP_DIR = /tmp/quarto
THEME = metropolis
PDFTK = pdftk  # Ensure pdftk is installed

# Find all markdown files in the current directory
MD_FILES = $(wildcard *.qmd)
PDF_FILES = $(patsubst %.qmd,$(OUTPUT_DIR)/%.pdf,$(MD_FILES))

# Default target
all: $(PDF_FILES)

# Rule to generate PDF from markdown and append the first page to the end
$(OUTPUT_DIR)/%.pdf: %.qmd
	mkdir -p $(OUTPUT_DIR) $(TEMP_DIR)
	$(PANDOC) $< -t beamer -V theme:$(THEME) -o $(patsubst %.qmd,%.pdf,$<) --highlight-style=espresso
	mv $(patsubst %.qmd,%.pdf,$<) $(OUTPUT_DIR)
	$(PDFTK) $(OUTPUT_DIR)/$(patsubst %.qmd,%.pdf,$<) cat 1 output $(TEMP_DIR)/first-page.pdf
	$(PDFTK) $(OUTPUT_DIR)/$(patsubst %.qmd,%.pdf,$<) $(TEMP_DIR)/first-page.pdf cat output $(TEMP_DIR)/final.pdf
	mv $(TEMP_DIR)/final.pdf $(OUTPUT_DIR)/$(patsubst %.qmd,%.pdf,$<)

# Clean up generated files
clean:
	rm -f $(PDF_FILES)
	rm -rf $(TEMP_DIR)
