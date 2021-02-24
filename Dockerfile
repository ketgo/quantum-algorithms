FROM jupyter/scipy-notebook

USER root

# Install Jupyter Notebook Extensions
RUN pip install --no-cache-dir jupyter_contrib_nbextensions && jupyter contrib nbextension install 

# Install Qiskit
RUN pip3 install --no-cache-dir qiskit && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    rm -rf /root/.cache

USER $NB_UID

# Remove work dir
RUN rm -r ~/work

