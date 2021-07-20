import numpy as np
import matplotlib.pyplot as plt

def show_example(X, y, y_pred=None, *, nrow=2, ncol=6):
    y = y.ravel()
    sample_indices = np.random.choice(X.shape[0], size=nrow*ncol, replace=False)
    title = 'Sample Predictions' if y_pred is not None else 'Sample Images'

    fig, axs = plt.subplots(nrows=nrow, ncols=ncol)
    fig.suptitle(title, fontsize='x-large')
    fig.set_size_inches(ncol*2, nrow*2 + 1)
    axs = axs.ravel()
    for ax_idx, im_idx in enumerate(sample_indices):
        image = X[im_idx].reshape(28, 28)
        axs[ax_idx].imshow(image)
        axs[ax_idx].get_xaxis().set_visible(False)
        axs[ax_idx].get_yaxis().set_visible(False)
        if y_pred is None:
            axs[ax_idx].set_title(f"Label: {y[im_idx]}")
        else:
            out_org, out_pred = y[im_idx], y_pred[im_idx]
            axs[ax_idx].set_title(f"Actual Label: {out_org}\n" \
                                  f"Predicted Label: {out_pred}", 
                            color='green' if out_org == out_pred else 'red')
    fig.tight_layout(rect=[0.05, 0.05, 0.95, 0.95])
    fig.show()

def plot_training_history(training_history, title='Training History'):
    train_loss = training_history.history['loss']
    valid_loss = training_history.history['val_loss']
    train_acc = training_history.history['accuracy']
    valid_acc = training_history.history['val_accuracy']

    fig, (ax1, ax2) = plt.subplots(1, 2)
    fig.suptitle(title)
    fig.set_size_inches(15, 5)

    ax1.plot(train_loss, label='Training Loss')
    ax1.plot(valid_loss, label='Validation Loss')
    ax1.set_title('Loss')
    ax1.legend()

    ax2.plot(train_acc, label='Training Accuracy')
    ax2.plot(valid_acc, label='Validation Accuracy')
    ax2.set_title('Accuracy')
    ax2.legend()

    fig.show()