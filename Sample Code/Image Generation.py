import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 6))

# Set limits and remove axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Define colors
grid_color = '#FFDDC1'
flexbox_color = '#C1E1FF'
text_color = '#333333'

# Add a title
fig.suptitle('Building a Responsive Website: Mastering CSS Grid and Flexbox', fontsize=16, weight='bold', color=text_color)

# Add Grid area
grid = patches.FancyBboxPatch((0, 3), 4, 2, boxstyle="round,pad=0.3", edgecolor=grid_color, facecolor=grid_color)
ax.add_patch(grid)
ax.text(2, 4, 'CSS Grid', ha='center', va='center', fontsize=14, weight='bold', color=text_color)

# Add Flexbox area
flexbox = patches.FancyBboxPatch((6, 3), 4, 2, boxstyle="round,pad=0.3", edgecolor=flexbox_color, facecolor=flexbox_color)
ax.add_patch(flexbox)
ax.text(8, 4, 'Flexbox', ha='center', va='center', fontsize=14, weight='bold', color=text_color)

# Add a connecting arrow
arrow = patches.FancyArrowPatch((4, 4), (6, 4), mutation_scale=20, color=text_color, linewidth=2)
ax.add_patch(arrow)

# Add a subtitle
ax.text(5, 2, 'Responsive Design Techniques', ha='center', va='center', fontsize=12, weight='medium', color=text_color)

# Save the image
file_path = "./image.png"
plt.savefig(file_path, bbox_inches='tight')
file_path
