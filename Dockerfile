FROM jupyter/scipy-notebook

USER root

# Install Qiskit
RUN pip3 install --no-cache-dir qiskit && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    rm -rf /root/.cache

USER $NB_UID

# Remove work dir
RUN rm -r ~/work

